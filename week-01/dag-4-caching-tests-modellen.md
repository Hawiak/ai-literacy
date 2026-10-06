# Dag 4 (za 10 okt, 2 uur): caching, fouten, tests en modelvergelijking

## Doel

Je bouwt de bouwstenen die elk LLM-systeem nodig heeft: kosten beheersen met caching, nette foutafhandeling, kleine geautomatiseerde tests (mini-evals) en een meting waarmee je twee modellen vergelijkt op kwaliteit, snelheid en kosten.

## Klaar als

- Je hebt met `cache_demo.py` zowel `cache_creation_input_tokens` als `cache_read_input_tokens` gezien.
- `t1/llm.py` bevat een `ask()` met foutafhandeling, timeout en retries.
- `uv run pytest` draait 5 mini-evals en ze slagen.
- Je README heeft een tabel die Haiku en Sonnet vergelijkt.

## Voorbereiding (5 min)

Maak deze structuur in `llm-lab`:

```text
llm-lab/
├── pyproject.toml
├── t1/
│   ├── __init__.py       (leeg)
│   ├── llm.py
│   ├── cases.py
│   ├── cache_demo.py
│   └── compare_models.py
└── tests/
    └── test_mini_eval.py
```

Voeg dit toe aan `pyproject.toml` zodat `pytest` je package vindt:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
```

## Deel 1: prompt caching (30 min)

**Idee.** Als elke call dezelfde lange instructie bevat (regels, documentatie, voorbeelden), betaal je die elke keer opnieuw. Met caching markeer je dat vaste stuk. De eerste call schrijft het naar een cache, volgende calls lezen het tegen een fractie van de kosten en meestal sneller. Er zijn voorwaarden: het gecachete stuk moet minstens een bepaald aantal tokens lang zijn, het moet **identiek** zijn, en de cache leeft beperkt lang. Lees de actuele regels en prijzen in de documentatie.

Maak `t1/cache_demo.py`:

```python
import time

import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-sonnet-5-5"

# Kunstmatig lange, vaste instructie (duizenden tokens) voor de demo.
INSTRUCTIE = " ".join(
    f"Regel {i}: antwoord altijd beknopt, noem eerst de conclusie en geef daarna"
    f" maximaal twee voorbeelden uit backend-ontwikkeling."
    for i in range(1, 151)
)


def ask(vraag: str) -> None:
    start = time.perf_counter()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=200,
        system=[
            {
                "type": "text",
                "text": INSTRUCTIE,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": vraag}],
    )
    ms = (time.perf_counter() - start) * 1000
    u = resp.usage
    print(
        f"{ms:6.0f} ms | invoer={u.input_tokens} "
        f"cache_write={u.cache_creation_input_tokens} "
        f"cache_read={u.cache_read_input_tokens} uit={u.output_tokens}"
    )


for vraag in ["Wat is idempotentie?", "Wat is een dead-letter queue?", "Wat is backpressure?"]:
    ask(vraag)
```

Draai `uv run t1/cache_demo.py` en let op:

- Call 1: `cache_write` is groot (de instructie wordt opgeslagen).
- Call 2 en 3: `cache_read` is groot, `invoer` klein.
- Zijn beide nul? Dan is je instructie te kort voor dit model. Verhoog `range(1, 151)` of controleer de minimale lengte in de documentatie.

**Experimenten.**

1. Verander één woord in `INSTRUCTIE` en draai opnieuw. Wat gebeurt er met `cache_read`? (De cache raakt ongeldig; het stuk moet identiek zijn.)
2. Wacht enkele minuten en draai opnieuw. Is de cache nog warm? Vergelijk met wat de documentatie over de levensduur zegt.
3. Reken uit hoeveel je bespaart bij 100 calls. Zoek de prijzen voor invoer, cache-schrijven en cache-lezen in de documentatie en schrijf de berekening in je `notes.md`. Dit is een algebra-oefening in het wild: kosten = aantal × prijs.

## Deel 2: een nette `ask()` met foutafhandeling (30 min)

Een demo gaat uit van succes; een echt systeem niet. Je vangt de drie hoofdsoorten fouten af en geeft ze een duidelijke betekenis.

Maak `t1/llm.py`:

```python
import time
from dataclasses import dataclass

import anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-sonnet-5-5"
# timeout en retries zijn bewuste keuzes, geen standaardwaarden om blind te vertrouwen
client = anthropic.Anthropic(timeout=30.0, max_retries=3)


@dataclass
class Antwoord:
    tekst: str
    input_tokens: int
    output_tokens: int
    stop_reason: str
    ms: float


def ask(
    vraag: str,
    model: str = MODEL,
    max_tokens: int = 300,
    system: str | None = None,
) -> Antwoord:
    kwargs: dict = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": vraag}],
    }
    if system:
        kwargs["system"] = system

    start = time.perf_counter()
    try:
        resp = client.messages.create(**kwargs)
    except anthropic.RateLimitError as e:
        raise RuntimeError("Rate limit bereikt; probeer het later opnieuw.") from e
    except anthropic.APIConnectionError as e:
        raise RuntimeError("Geen verbinding met de API.") from e
    except anthropic.APIStatusError as e:
        raise RuntimeError(f"API-fout {e.status_code}: {e.message}") from e
    ms = (time.perf_counter() - start) * 1000

    if resp.stop_reason == "max_tokens":
        print("Waarschuwing: antwoord is afgekapt (max_tokens).")

    return Antwoord(
        tekst=resp.content[0].text,
        input_tokens=resp.usage.input_tokens,
        output_tokens=resp.usage.output_tokens,
        stop_reason=resp.stop_reason,
        ms=ms,
    )
```

**Waarom zo?**

- De SDK probeert bij tijdelijke fouten zelf opnieuw (`max_retries`). Je kiest het aantal bewust.
- `timeout` voorkomt dat je programma eindeloos wacht.
- Je vertaalt API-fouten naar eigen, duidelijke meldingen. Dat maakt de rest van je code eenvoudiger.
- Je controleert `stop_reason`. Een afgekapt antwoord is geen succes.

**Experiment.** Zet in een testscript tijdelijk een foute key (`anthropic.Anthropic(api_key="fout")`) en kijk welke melding je krijgt. Zet daarna een erg lage `timeout=0.001` en kijk wat er gebeurt. Zet beide daarna terug.

## Deel 3: mini-evals met pytest (30 min)

Een eval is een test voor gedrag. Dit is de allereerste, kleinste versie ervan: vijf vragen met een verwachte term in het antwoord.

Maak `t1/cases.py`:

```python
CASES = [
    ("Wat is de hoofdstad van Frankrijk? Antwoord met één woord.", "parijs"),
    ("Wat is 17 * 3? Antwoord alleen met het getal.", "51"),
    ("Welke HTTP-statuscode hoort bij 'Not Found'? Alleen het getal.", "404"),
    ("In welke taal is NestJS geschreven? Eén woord.", "typescript"),
    ("Wat is de afkorting van JSON Web Token? Alleen de afkorting.", "jwt"),
]
```

Maak `tests/test_mini_eval.py`:

```python
import pytest

from t1.cases import CASES
from t1.llm import ask


@pytest.mark.parametrize("vraag,verwacht", CASES)
def test_antwoord_bevat_verwachte_term(vraag, verwacht):
    antwoord = ask(vraag, max_tokens=50, system="Antwoord zo kort mogelijk.")
    assert verwacht in antwoord.tekst.lower()
```

Draai: `uv run pytest -v`. Alles groen? Probeer dan:

1. Maak één case expres fout (verwacht `"londen"` bij Frankrijk) en kijk hoe de falende test eruitziet.
2. Voeg twee eigen cases toe over iets uit jouw werk, zonder bedrijfsdata.
3. Draai de tests drie keer. Zijn de resultaten steeds gelijk? Zo niet, wat zegt dat over variatie in modeluitvoer?

**Let op.** Deze tests roepen de echte API aan en kosten dus een paar tokens. Dat is acceptabel voor 5 cases; bij honderden cases wil je een eval-runner met kostenbewaking (tutorial 3).

## Deel 4: Haiku tegen Sonnet (25 min)

Maak `t1/compare_models.py`:

```python
from t1.cases import CASES
from t1.llm import ask

MODELLEN = ["claude-haiku-4-5-20251001", "claude-sonnet-5-5"]

# Vul de prijzen in dollars per miljoen tokens in uit de officiële prijspagina.
PRIJZEN = {
    "claude-haiku-4-5-20251001": {"in": None, "uit": None},
    "claude-sonnet-5-5": {"in": None, "uit": None},
}


def kosten(model: str, tokens_in: int, tokens_uit: int) -> float | None:
    p = PRIJZEN[model]
    if p["in"] is None or p["uit"] is None:
        return None
    return tokens_in / 1_000_000 * p["in"] + tokens_uit / 1_000_000 * p["uit"]


print("| model | goed | gem. ms | tokens in | tokens uit | kosten ($) |")
print("| --- | --- | --- | --- | --- | --- |")
for model in MODELLEN:
    goed = ms = tin = tuit = 0
    for vraag, verwacht in CASES:
        a = ask(vraag, model=model, max_tokens=50, system="Antwoord zo kort mogelijk.")
        goed += verwacht in a.tekst.lower()
        ms += a.ms
        tin += a.input_tokens
        tuit += a.output_tokens
    k = kosten(model, tin, tuit)
    kosten_tekst = f"{k:.6f}" if k is not None else "vul prijzen in"
    print(f"| {model} | {goed}/{len(CASES)} | {ms / len(CASES):.0f} | {tin} | {tuit} | {kosten_tekst} |")
```

Draai het, vul de prijzen in en plak de uitvoer in je README onder het kopje "Modelvergelijking". Voeg een paar zinnen toe:

- Welk model was sneller en hoeveel?
- Waren er cases waarin ze verschilden?
- Wat zou je kiezen voor een eenvoudige classificatietaak, en waarom?

De vergelijking met 5 vragen zegt weinig statistisch. Dat is precies het punt: schrijf ook op wat je met zo'n kleine steekproef **niet** kunt concluderen.

## Zelftest

1. Wat moet waar zijn zodat prompt caching werkt?
2. Waarom controleer je `stop_reason` in `ask()`?
3. Welk probleem lost `max_retries` op, en welk probleem niet?
4. Waarom is een test met 5 cases niet genoeg om modellen eerlijk te vergelijken?
5. Hoe bereken je de kosten van een call als de prijs per miljoen tokens is gegeven?

<details>
<summary>Antwoorden</summary>

1. Het gemarkeerde stuk moet lang genoeg zijn, exact hetzelfde blijven en binnen de levensduur van de cache opnieuw worden gebruikt.
2. Een afgekapt antwoord (`max_tokens`) is onvolledig en mag niet als compleet resultaat worden behandeld.
3. Het lost tijdelijke fouten op (netwerk, overbelasting); het lost geen foute key, ongeldige invoer of een structureel te traag antwoord op.
4. De steekproef is te klein en de cases te eenvoudig; kleine verschillen kunnen toeval zijn.
5. kosten = tokens_in / 1.000.000 × prijs_in + tokens_uit / 1.000.000 × prijs_uit.

</details>

## Afsluiten

```bash
uv run ruff check .
uv run pytest
git add -A
git commit -m "dag 4: caching, ask() met foutafhandeling, mini-evals en modelvergelijking"
git push
```

Logboekregel schrijven en dag 4 afvinken.

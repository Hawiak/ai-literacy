1# Dag 1 (wo 7 okt, 45 min): omgeving en eerste API-call

## Doel

Een werkende Python-omgeving, een veilig opgeslagen API-key en je eerste antwoord van Claude, met begrip van wat er in het antwoord zit.

## Klaar als

- `uv run t1/hello.py` print een antwoord, het tokengebruik en de `stop_reason`.
- `git check-ignore .env` print `.env` (het bestand wordt dus genegeerd).
- Je eerste commit staat op GitHub zonder geheimen.

## Waarom deze volgorde

Je zet `.gitignore` neer **voordat** je de key aanmaakt. Een key die één keer in een commit heeft gestaan, staat in de geschiedenis, ook als je het bestand later verwijdert. Dan moet je de key intrekken. Voorkomen is eenvoudiger dan opruimen.

## Stap 1: uv installeren (5 min)

`uv` is een snelle Python-pakketbeheerder die ook de Python-versie en de virtuele omgeving regelt.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
```

Heb je `uv` al, sla dit over. Open daarna een nieuwe terminal zodat het commando gevonden wordt.

## Stap 2: repo en project aanmaken (10 min)

Maak de repo `ai-literacy` met de bestanden die je al hebt (`README.md`, `logboek.md`, `week-01/`, `wiskunde/`). Hernoem `_gitignore` naar `.gitignore`.

```bash
cd ai-literacy
mv _gitignore .gitignore        # alleen als dit bestand er staat
git init
git add .gitignore README.md logboek.md
git commit -m "start: repo-structuur en gitignore"

uv init llm-lab
cd llm-lab
uv add anthropic python-dotenv
uv add --dev pytest ruff
mkdir t1 tests
```

`uv init` maakt `pyproject.toml` en een `.python-version` aan. `uv add` schrijft afhankelijkheden daarin en maakt een `.venv`. Gebruik voortaan `uv run <script>` zodat de juiste omgeving wordt gebruikt zonder dat je iets hoeft te activeren.

## Stap 3: API-key aanmaken en opslaan (10 min)

1. Log in op de Anthropic Console (console.anthropic.com) en maak een API-key aan. Geef hem een herkenbare naam, bijvoorbeeld `llm-lab-laptop`.
2. Stel een **uitgavenlimiet** in. Zoek in de Console onder de instellingen voor limieten of facturering naar een maandlimiet en kies een laag bedrag. Controleer de actuele opties in de documentatie; de plaats van deze instelling kan veranderen.
3. Sla de key op in `llm-lab/.env`:

```text
ANTHROPIC_API_KEY=sk-ant-...
```

4. Maak ook een `.env.example` aan zonder echte waarde, zodat je later weet welke variabelen nodig zijn:
:q

```text
ANTHROPIC_API_KEY=
```

5. Controleer dat `.env` genegeerd wordt:

```bash
git check-ignore -v .env
git status
```

`git status` mag `.env` niet als nieuw bestand tonen. Zie je het wel, stop dan en kijk naar je `.gitignore` voordat je iets commit.

## Stap 4: je eerste call (10 min)

Maak `t1/hello.py` en typ het zelf over:

```python
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()  # leest ANTHROPIC_API_KEY uit de omgeving

response = client.messages.create(
    model="claude-sonnet-5-5",  # controleer de actuele naam in de documentatie
    max_tokens=500,
    messages=[{"role": "user", "content": "Leg event sourcing uit in drie zinnen."}],
)

for block in response.content:
    if block["type"] == "message":
        print(block["message"]["content"])
print("tokens:", response.usage.input_tokens, "in,", response.usage.output_tokens, "uit")
print("stop_reason:", response.stop_reason)
```

Draai het:

```bash
uv run t1/hello.py
```

## Stap 5: lees het antwoord als programmeur (5 min)

Print eens het hele object: `print(response)`. Je ziet onder andere:

- `content`: een **lijst** van blokken, geen losse string. Een antwoord kan tekst en later ook `tool_use`-blokken bevatten.
- `usage`: het aantal invoer- en uittokens. Daar betaal je voor.
- `stop_reason`: waarom het model stopte (`end_turn`, `max_tokens`, `tool_use`, ...).
- `model` en `id`: handig om te loggen.

## Experimenten (5 min)

Schrijf je waarnemingen in het logboek.

1. Zet `max_tokens` op 20. Wat gebeurt er met het antwoord en met `stop_reason`?
2. Vraag hetzelfde in het Engels en in het Nederlands. Verschilt het aantal tokens?
3. Vraag iets heel kort (`Zeg hallo.`) en iets lang. Hoe verhouden de uitvoertokens zich tot de lengte van het antwoord?

## Als het niet werkt

| Melding | Waarschijnlijke oorzaak | Oplossing |
| --- | --- | --- |
| `authentication_error` of 401 | Key ontbreekt of is fout | Controleer `.env` en of je in `llm-lab` draait |
| `not_found_error` bij het model | Modelnaam klopt niet meer | Zoek de actuele naam in de documentatie |
| `ModuleNotFoundError` | Je gebruikt `python` in plaats van `uv run` | Draai met `uv run t1/hello.py` |
| `rate_limit_error` | Te veel calls of een laag account | Even wachten en opnieuw proberen |

## Zelftest

1. Waarom komt `.gitignore` vóór de API-key?
2. Wat is het verschil tussen `uv add` en `uv add --dev`?
3. Waarom is `response.content` een lijst?
4. Welke twee getallen bepalen de kosten van een call?

<details>
<summary>Antwoorden</summary>

1. Een key in een commit staat voor altijd in de geschiedenis; je kunt hem dan alleen nog intrekken.
2. `--dev` voegt pakketten toe die alleen voor ontwikkeling zijn (tests, linting), niet voor het draaien van je code.
3. Een antwoord kan uit meerdere blokken bestaan, bijvoorbeeld tekst en tool-aanroepen.
4. Het aantal invoer- en uitvoertokens (`usage`), tegen de prijs van het gekozen model.

</details>

## Afsluiten

```bash
git add -A
git commit -m "dag 1: omgeving en eerste API-call"
git push
```

Voeg een regel toe aan `logboek.md` en vink dag 1 af in `week-01/README.md`.

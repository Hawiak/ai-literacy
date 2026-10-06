# Dag 6 (ma 12 okt, 45 min): Home Assistant lezen via de API

## Doel

Je leest echte waarden uit je eigen huis met een klein Python-script. Dit is de eerste stap naar de thuisassistent in tutorial 4: eerst de data begrijpen, daarna pas een model erbij halen.

## Klaar als

- Een `curl`-test met je token geeft `{"message":"API running."}`.
- `huis/ha.py` print het aantal entiteiten per domein en de toestand van 3 entiteiten die je zelf kiest.
- Je token staat in `.env` en nergens anders.

## Waarom dit nu

Een agent is maar zo goed als zijn tools, en een tool is maar zo goed als je begrijpt wat de data eronder doet. Als je weet hoe `/api/states` eruitziet, hoe groot het resultaat is en welke velden bruikbaar zijn, ontwerp je later betere tools. Je gebruikt vandaag **geen** LLM.

## Stap 1: token aanmaken (10 min)

In Home Assistant: klik linksonder op je profiel, ga naar het tabblad **Beveiliging** en scrol naar **Langdurige toegangstokens**. Maak een token aan met de naam `llm-lab`. Het token wordt **één keer** getoond: kopieer het meteen naar je `.env`. Namen van menu's kunnen per versie en taalinstelling verschillen.

Voeg toe aan `llm-lab/.env`:

```text
HA_URL=http://homeassistant.local:8123
HA_TOKEN=...
```

Gebruik je eigen lokale adres als dat anders is. Voeg `HA_URL=` en `HA_TOKEN=` (zonder waarde) toe aan `.env.example`.

**Veiligheid.** Dit token geeft toegang tot je huis. Deel het nooit, zet het niet in een screenshot of commit en geef je Home Assistant niet vrij op het internet voor dit experiment. Je kunt het token op elk moment verwijderen in hetzelfde scherm. Overweeg later een apart, beperkt account voor je projecten.

## Stap 2: testen met curl (5 min)

```bash
cd llm-lab
set -a; source .env; set +a
curl -s -H "Authorization: Bearer $HA_TOKEN" "$HA_URL/api/"
```

Verwacht: `{"message":"API running."}`. Krijg je een 401, dan klopt het token niet; krijg je geen verbinding, controleer dan het adres en of je op hetzelfde netwerk zit.

Bekijk een enkele entiteit, bijvoorbeeld een sensor die je kent:

```bash
curl -s -H "Authorization: Bearer $HA_TOKEN" "$HA_URL/api/states/sensor.JOUW_SENSOR"
```

Je krijgt een JSON-object met `entity_id`, `state`, `attributes`, `last_changed` en `last_updated`. Kijk goed naar de velden; alles wat je later in tools gebruikt, komt hieruit.

## Stap 3: het script (15 min)

```bash
uv add httpx
mkdir huis
```

Maak `huis/ha.py` en typ het zelf:

```python
import os
import sys
from collections import Counter

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE = os.environ["HA_URL"].rstrip("/")
HEADERS = {"Authorization": f"Bearer {os.environ['HA_TOKEN']}"}


def get(pad: str):
    r = httpx.get(f"{BASE}{pad}", headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()


def states() -> list[dict]:
    return get("/api/states")


def state(entity_id: str) -> dict:
    return get(f"/api/states/{entity_id}")


def main() -> None:
    print(get("/api/")["message"])

    alle = states()
    domeinen = Counter(s["entity_id"].split(".")[0] for s in alle)
    print(f"{len(alle)} entiteiten")
    for domein, aantal in domeinen.most_common():
        print(f"{domein:22s} {aantal}")

    for entity_id in sys.argv[1:4]:
        s = state(entity_id)
        naam = s["attributes"].get("friendly_name")
        print(f"{entity_id}: {s['state']} ({naam}) sinds {s['last_changed']}")


if __name__ == "__main__":
    main()
```

Draai: `uv run huis/ha.py sensor.een light.twee climate.drie` met drie entiteiten die in jouw huis bestaan.

Kijk naar wat je ziet:

- Welke domeinen komen het meest voor? Verrast je dat?
- Hoeveel van de entiteiten zijn eigenlijk "technisch" (bijvoorbeeld update-entiteiten) en weinig interessant voor een vraag als "waarom ging de airco aan?"
- Zit er in `friendly_name` iets persoonlijks of iets wat je niet naar een externe API zou willen sturen?

## Stap 4: uitbreidingen (10 min, kies er één of twee)

1. **Nette fout.** Vraag een entiteit op die niet bestaat. Je krijgt een `httpx.HTTPStatusError` met een 404. Vang die af en print een heldere melding in plaats van een lange traceback.
2. **Tijd in lokale tijd.** `last_changed` is in UTC. Zet hem om naar Amsterdamse tijd:

```python
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.fromisoformat(s["last_changed"]).astimezone(ZoneInfo("Europe/Amsterdam"))
print(dt.strftime("%Y-%m-%d %H:%M"))
```

3. **Numerieke sensoren.** Filter alle `sensor.*` met een `unit_of_measurement` en een getal als `state`, en print de eerste tien. Wat valt op aan de eenheden?
4. **Laatst gewijzigd.** Welke 5 entiteiten veranderden het laatst? (Sorteer op `last_changed`.)

## Waarom dit relevant is voor LLM's

De volledige uitvoer van `/api/states` is te groot om aan een model te geven en bevat veel ruis. Een goede tool geeft een **compacte samenvatting**: een paar treffers, kernvelden en eventueel een berekende waarde zoals het gemiddelde. Het meten en filteren dat je nu met de hand doet, zit later in je tools.

## Zelftest

1. Waarom test je met `curl` voordat je Python schrijft?
2. Welke velden van een entiteit zijn voor een vraag als "wanneer ging X aan?" het nuttigst?
3. Waarom wil je een token niet delen, en wat doe je als dat toch gebeurt?
4. Waarom is een volledige lijst van alle entiteiten ongeschikt als invoer voor een model?

<details>
<summary>Antwoorden</summary>

1. Je scheidt netwerk- en tokenproblemen van codefouten.
2. `state`, `last_changed` en `attributes` (vooral `friendly_name` en eenheden).
3. Het geeft toegang tot je huis. Verwijder het token in Home Assistant en maak een nieuw token aan.
4. Het is groot, vol ruis en kost veel tokens; een model heeft een beperkte, gerichte selectie nodig.

</details>

## Afsluiten

Commit **geen** uitvoer die entiteitsnamen met persoonlijke betekenis bevat. Voeg eventueel `huis/uitvoer/` toe aan `.gitignore` als je uitvoer opslaat.

```bash
git add -A
git commit -m "dag 6: Home Assistant API lezen met httpx"
git push
```

Logboekregel schrijven en dag 6 afvinken.

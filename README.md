# AI-literacy jaar

Mijn repo voor een jaar AI-literacy: begrijpen hoe AI werkt, het toepassen en eraan werken. Hier staan mijn tutorials, code, logboek en voortgang.

## Structuur

```text
.
├── README.md        dit bestand
├── logboek.md       een paar regels per sessie
├── week-01/         dagtutorials en voortgang van week 1
├── wiskunde/        algebralessen met oefeningen en uitwerkingen
└── llm-lab/         alle code (uv-project)
    ├── t1/          scripts van tutorial 1
    └── tests/       pytest-tests en mini-evals
```

## Zo werk je per sessie

1. Open het bestand van de dag (`week-01/dag-N-....md`) en lees eerst **Doel** en **Klaar als**.
2. Doe de stappen. Typ de code zelf over; kopieer alleen als je het begrijpt.
3. Doe de experimenten en schrijf op wat je zag. Dat is waar het leren zit.
4. Beantwoord de zelftest zonder te kijken en vergelijk daarna met de antwoorden.
5. Voeg een regel toe aan `logboek.md` en vink de dag af in `week-01/README.md`.
6. Commit: `git add -A && git commit -m "dag 2: eerste calls en streaming"`.

## Voortgang

De voortgang per week staat als afvinklijst in de README van die week. Het logboek is de ruwe versie, de week-README de samenvatting.

## Vaste regels

- **Nooit een API-key, token of wachtwoord in git.** `.env` staat in `.gitignore` vanaf de eerste commit. Is er toch iets gelekt: trek de sleutel direct in en maak een nieuwe aan.
- **Geen persoonlijke of werkgerelateerde data in dit project.** Gebruik nepdata of eigen data zonder adressen, namen van personen of bedrijfsgegevens. Alles wat je naar een API stuurt, verlaat je computer.
- **Elke sessie eindigt met een commit** en een logboekregel, ook als het klein is.
- **Houd je uitgaven in de gaten** in de Anthropic Console, zeker de eerste weken.
- **Controleer modelnamen en prijzen** in de officiële documentatie. Ze veranderen vaker dan deze bestanden.

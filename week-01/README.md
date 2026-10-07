# Week 1: fundament (7 tot 13 oktober 2026)

Aan het eind van deze week heb je een werkende API-chat met streaming en caching, een paar tests, je eerste stukken algebra en backpropagation, en een script dat echte waarden uit je huis leest. Plus een logboek en een repo die je kunt laten zien.

## Schema

| Dag | Duur | Bestand | Waar het over gaat |
| --- | --- | --- | --- |
| Wo 7 okt | 45 min | [dag-1-omgeving.md](dag-1-omgeving.md) | Omgeving, API-key, eerste call |
| Do 8 okt | 1,5 uur | [dag-2-eerste-calls.md](dag-2-eerste-calls.md) | Berichten, system prompt, streaming |
| Vr 9 okt | 45 min | [dag-3-vacatures-en-algebra.md](dag-3-vacatures-en-algebra.md) | Vacatures lezen en algebra les 1 |
| Za 10 okt | 2 uur | [dag-4-caching-tests-modellen.md](dag-4-caching-tests-modellen.md) | Caching, fouten, tests, modelvergelijking |
| Zo 11 okt | 1,5 uur | [dag-5-micrograd.md](dag-5-micrograd.md) | Algebra les 2 en afgeleiden met micrograd |
| Ma 12 okt | 45 min | [dag-6-home-assistant.md](dag-6-home-assistant.md) | Home Assistant lezen via de API |
| Di 13 okt | 1 uur | [dag-7-review-en-algebra.md](dag-7-review-en-algebra.md) | Weekreview en algebra les 3 |

De algebralessen staan in [../wiskunde/](../wiskunde/). Totaal ongeveer 8,25 uur.

## Voortgang

### Dag 1: omgeving
- [x] `uv` geïnstalleerd en project `llm-lab` aangemaakt
- [x] API-key in `.env`, uitgavenlimiet ingesteld
- [x] `git check-ignore .env` bevestigt dat `.env` genegeerd wordt
- [x] `hello.py` print antwoord en tokengebruik
- [x] Eerste commit gepusht

### Dag 2: eerste calls
- [x] Je kunt in eigen woorden uitleggen waarom de API *stateless* is
- [x] `chat.py` met system prompt, meerdere beurten en streaming
- [x] `/reset` en een tokenteller per sessie
- [x] Experimenten met `max_tokens` en `temperature` genoteerd

### Dag 3: vacatures en algebra
- [ ] 3 vacatures gelezen, `notes.md` ingevuld
- [ ] Algebra les 1 gedaan, minstens 6 van 8 oefeningen goed

### Dag 4: caching, tests, modellen
- [ ] Caching gemeten (creation- en read-tokens gezien)
- [ ] Foutafhandeling in je client
- [ ] 5 mini-evals met `pytest`
- [ ] Vergelijking Haiku tegen Sonnet in een tabel in je README

### Dag 5: micrograd
- [ ] Algebra les 2 gedaan, minstens 6 van 8 oefeningen goed
- [ ] Numerieke afgeleide zelf geprogrammeerd en uitgelegd
- [ ] Micrograd: eerste deel gekeken en meegecodeerd
- [ ] Je legt de kettingregel uit met een eigen voorbeeld

### Dag 6: Home Assistant
- [ ] Token aangemaakt en `curl`-test geslaagd
- [ ] `ha.py` print 3 echte entiteiten
- [ ] Overzicht van domeinen en aantallen gemaakt

### Dag 7: review en algebra
- [ ] Algebra les 3 gedaan, minstens 5 van 6 oefeningen goed
- [ ] Zelftest van de week ingevuld
- [ ] 3 leerpunten in deze README
- [ ] Alles gepusht, planning week 2 gemaakt

## Eindcriteria van de week

- Je legt uit wat een token, een system prompt en `stop_reason` zijn.
- Je legt uit wat een afgeleide en een loss zijn, in gewone woorden.
- Je repo bevat `llm-lab` met werkende scripts, tests en een README met je vergelijkingstabel.
- Je logboek heeft minstens 6 regels.

## Als je vastloopt

1. Lees de foutmelding helemaal en kijk naar de laatste regel eerst.
2. Zoek de foutcode of -tekst op in de documentatie.
3. Verklein het probleem: een script van 5 regels dat het probleem toont.
4. Na 20 minuten zonder voortgang: noteer wat je geprobeerd hebt in het logboek en ga door met het volgende onderdeel. Vaak zie je de volgende dag direct wat er mis was.

Vastlopen hoort bij leren; het is geen teken dat je het niet kunt.

## Uitgaven bewaken

De eerste weken kijk je dagelijks in de Console naar wat je uitgaf. Verwacht bij normaal oefenen enkele centen per sessie; zie je iets anders, zoek dan eerst uit waarom. Een `while`-loop die zichzelf blijft aanroepen of een ongewoon lange prompt is vaak de oorzaak.

## Mijn leerpunten van de week

1.
2.
3.

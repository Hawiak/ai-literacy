# Dag 7 (di 13 okt, 1 uur): weekreview en algebra les 3

## Doel

De week afronden: algebra les 3 (je ziet hoe een model, een fout en "leren" in een paar regels wiskunde passen), jezelf toetsen op wat je hebt geleerd en de volgende week plannen.

## Klaar als

- Les 3 van [../wiskunde/les-3-modellen-en-fouten.md](../wiskunde/les-3-modellen-en-fouten.md) is gedaan, met minstens 5 van de 6 oefeningen goed.
- De zelftest hieronder is ingevuld en nagekeken.
- `week-01/README.md` bevat 3 leerpunten en alle afgeronde dagen zijn afgevinkt.
- Je repo staat op GitHub zonder geheimen en je weet wat je volgende week gaat doen.

## Deel 1: algebra les 3 (30 min)

Open [../wiskunde/les-3-modellen-en-fouten.md](../wiskunde/les-3-modellen-en-fouten.md). Dit is de les waarin alles samenkomt: een model als formule `y = w·x + b`, een fout (loss) en de vraag welke `w` en `b` de fout kleinst maken. Het gaat om dezelfde afgeleiden en dalen als zondag.

## Deel 2: zelftest van de week (15 min)

Beantwoord zonder te kijken, op papier of in `notes.md`.

1. Waarom is de API stateless, en wat betekent dat voor kosten bij lange gesprekken?
2. Wat is het verschil tussen de system prompt en een user-bericht?
3. Wat vertelt `stop_reason` je, en welke waarde is een waarschuwing?
4. Wat moet waar zijn voor prompt caching?
5. Waarom is een mini-eval met 5 cases een goed begin maar geen bewijs?
6. Wat is een afgeleide, in gewone woorden?
7. Wat doet gradient descent, en wat gaat er mis bij een te grote leersnelheid?
8. Leg de kettingregel uit met een eigen voorbeeld.
9. Wat is een loss, en waarom wil je hem klein hebben?
10. Waarom geef je een model geen ruwe `/api/states` van Home Assistant?

<details>
<summary>Antwoorden</summary>

1. Elke call is op zichzelf staand, dus je stuurt de hele `history` mee; invoertokens en kosten groeien daardoor per beurt.
2. De system prompt stelt rol en regels voor het hele gesprek; een user-bericht is één beurt.
3. Waarom het model stopte; `max_tokens` is een waarschuwing want het antwoord is afgekapt.
4. Het gemarkeerde stuk is lang genoeg, identiek en wordt binnen de levensduur van de cache hergebruikt.
5. Het meet iets kleins en simpels en variatie speelt een grote rol; het geeft richting, geen statistische zekerheid.
6. De helling van een functie in één punt: hoe snel de uitkomst verandert als de invoer iets verandert.
7. Het past een getal stap voor stap aan in de richting waarin de fout daalt; te grote stappen schieten over het minimum heen en kunnen divergeren.
8. Bijvoorbeeld `y = (2x+1)²`: `y` verandert met `2g` als `g` verandert, `g` verandert met 2 als `x` verandert, samen `4g`.
9. Een getal dat aangeeft hoe fout het model zit; hoe kleiner, hoe beter de voorspellingen zijn.
10. Het is te groot, vol ruis, duur in tokens en kan gevoelige data bevatten; een tool moet compact en gericht zijn.

</details>

Scoor jezelf: 8 of meer goed is prima. Bij minder dan 6 herhaal je de bijbehorende dag volgende week voordat je verder gaat; dat is slimmer dan doorgaan met een gat.

## Deel 3: weekreview (10 min)

Vul in `week-01/README.md` onder "Mijn leerpunten van de week" drie punten in. Beantwoord daarnaast kort in het logboek:

- Wat kostte meer tijd dan gepland, en waarom?
- Welk onderdeel was het leukst, welk het saaist? (Beide zijn informatie.)
- Wat blijft onduidelijk en wil je volgende week opzoeken?
- Wat is je totaal aan uitgaven in de Console deze week?

Vink alle afgeronde onderdelen af in de voortgangslijst en laat open wat niet gelukt is; schuif dat bewust door naar volgende week in plaats van het te negeren.

## Deel 4: week 2 plannen (5 min)

Het plan voor week 2 (14 tot 20 oktober) is, afhankelijk van de uitkomst van deze week:

| Onderdeel | Duur | Wat |
| --- | --- | --- |
| Lezen | 30 min | Anthropic's *Building effective agents*; noteer 5 punten |
| Tutorial 2 | 3 tot 4 uur | Tool use en een eigen agent-loop met een huis-voorbeeld |
| Karpathy | 1,5 uur | *micrograd* afmaken, backpropagation in code |
| Algebra | 1 uur | Herhaal de oefeningen die fout gingen en maak extra oefeningen van Khan Academy |
| Review | 30 min | Logboek, commit, korte weekreview |

Kies tijdstippen in je agenda en zet ze er vast in. Pas dit plan aan op hoe deze week ging: liever een lichtere week 2 die je haalt dan een zware die je laat vallen.

## Afsluiten

```bash
git add -A
git commit -m "dag 7: weekreview en algebra les 3"
git push
```

Logboekregel schrijven en dag 7 afvinken. Klaar met week 1.

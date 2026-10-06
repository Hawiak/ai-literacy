# Dag 5 (zo 11 okt, 1,5 uur): algebra les 2 en afgeleiden met micrograd

## Doel

Begrijpen wat een afgeleide is (de helling van een functie in één punt) en hoe backpropagation die gebruikt om een netwerk te laten leren. Je doet het eerst met je handen en je eigen code, en kijkt daarna het eerste deel van Karpathy's micrograd.

## Klaar als

- Je hebt les 2 van [../wiskunde/les-2-functies-machten-logaritmen.md](../wiskunde/les-2-functies-machten-logaritmen.md) gedaan, met minstens 6 van de 8 oefeningen goed.
- Je hebt zelf een numerieke afgeleide geprogrammeerd en de uitkomst vergeleken met de formule.
- Je legt de kettingregel uit met een eigen voorbeeld.
- Je hebt de eerste helft van de micrograd-video gekeken en meegecodeerd.

## Deel 1: algebra les 2 (30 min)

Open [../wiskunde/les-2-functies-machten-logaritmen.md](../wiskunde/les-2-functies-machten-logaritmen.md) en volg het stappenplan: uitleg lezen met pen en papier, de codevoorbeelden draaien, de 8 oefeningen zonder uitwerkingen en daarna controleren. Les 2 bevat het idee dat je vandaag nodig hebt: een kromme heeft op elk punt een helling.

## Deel 2: afgeleiden zonder angst (25 min)

**Het idee.** Voor een rechte lijn `f(x) = 2x + 1` is de helling overal 2. Voor een kromme lijn verandert de helling per punt. De **afgeleide** in een punt is de helling op dat punt. Je kunt hem benaderen door een heel klein stapje `h` te zetten en te kijken hoeveel `f` verandert:

```text
helling ≈ (f(x + h) - f(x)) / h        voor een heel kleine h
```

Waarom is dit belangrijk? Een model leren betekent: een getal (een gewicht) zo aanpassen dat de fout kleiner wordt. De afgeleide van de fout naar dat gewicht vertelt **welke kant op** en **hoe sterk** je moet bijsturen. Dat is het hele idee achter training.

### Opdracht A: numerieke afgeleide

Maak `llm-lab/dag5/afgeleide.py` (houd per dag of onderwerp een eigen map, dan blijft je repo overzichtelijk):

```python
def f(x: float) -> float:
    return 3 * x**2 - 4 * x + 5


def afgeleide(f, x: float, h: float = 1e-6) -> float:
    return (f(x + h) - f(x)) / h


for x in [-2, 0, 2 / 3, 2, 3]:
    print(f"x={x:6.3f}  f(x)={f(x):8.3f}  helling≈{afgeleide(f, x):8.3f}")
```

Voorspel eerst, reken dan:

- De formule voor de afgeleide van deze functie is `6x - 4`. Vul deze in bij elk punt en vergelijk met je output.
- Bij welke x is de helling 0? Wat is daar bijzonder aan de functiewaarde? (Daar zit het minimum.)
- Wat betekent een negatieve helling? Beweeg je naar rechts, dan daalt of stijgt de functie?

Verwachte uitkomst:

| x | helling (6x − 4) |
| --- | --- |
| −2 | −16 |
| 0 | −4 |
| 2/3 | 0 |
| 2 | 8 |
| 3 | 14 |

### Opdracht B: één stap bergafwaarts

Als de helling negatief is, moet je naar rechts om lager uit te komen; is hij positief, dan naar links. Dat is **gradient descent**:

```python
x = 3.0
leersnelheid = 0.1
for stap in range(20):
    x = x - leersnelheid * afgeleide(f, x)
    print(f"stap {stap:2d}  x={x:.4f}  f(x)={f(x):.4f}")
```

Kijk waar `x` naartoe loopt (het minimum bij 2/3 ≈ 0.667). Probeer daarna `leersnelheid = 0.4` en `leersnelheid = 0.5`. Wat gebeurt er als de stap te groot is? Voor deze functie gaat het mis boven ongeveer 0.33: dan schiet elke stap over het minimum heen en wordt de afstand groter in plaats van kleiner. Dit is een van de belangrijkste lessen uit het trainen van modellen.

### Opdracht C: de kettingregel in gewone woorden

Soms zit de ene functie in de andere: `y = (2x + 1)²`. Noem `g = 2x + 1`, dan is `y = g²`.

- Hoe snel verandert `y` als `g` verandert? Dat is `2g`.
- Hoe snel verandert `g` als `x` verandert? Dat is `2`.
- Samen: hoe snel verandert `y` als `x` verandert? `2g · 2 = 4g = 4(2x + 1)`.

**Regel:** de snelheden van opeenvolgende stappen vermenigvuldig je. Controleer het numeriek:

```python
def y(x):
    return (2 * x + 1) ** 2

print(afgeleide(y, 1))   # verwacht ongeveer 12, want 4 * (2*1 + 1) = 12
print(afgeleide(y, -1))  # verwacht ongeveer -4, want 4 * (2*(-1) + 1) = -4
```

Backpropagation is deze regel, keer op keer, door een heel netwerk heen. Daarom heet het "terug"-propagatie: je rekent van het resultaat terug naar elk gewicht.

## Deel 3: micrograd kijken (30 min)

Zoek op YouTube naar Karpathy's video *The spelled-out intro to neural networks and backpropagation: building micrograd* (onderdeel van "Neural Networks: Zero to Hero"). Het is een lange video; je kijkt vandaag alleen het eerste deel, tot en met het stuk waarin hij **met de hand** de afgeleiden door een kleine som terugrekent.

**Hoe je kijkt.**

- Pauzeer vaak. Typ elke regel code over in `llm-lab/dag5/micrograd_notities.py` of in een notebook.
- Stop liever na 30 minuten met begrip dan na 90 minuten met stress.
- Lukt iets niet, noteer het in het logboek en kijk het deel de volgende keer opnieuw.

**Waar je op let** (controlepunten voor het eerste deel):

1. Hoe hij een afgeleide numeriek benadert, precies zoals in opdracht A.
2. Hoe hij een `Value`-object maakt dat een getal bijhoudt en onthoudt uit welke bewerkingen het ontstond.
3. Hoe de bewerkingen een **rekengraaf** vormen (een boom van optellingen en vermenigvuldigingen).
4. Hoe hij met de hand de afgeleide van elk knooppunt terugrekent met de kettingregel.

Als je bij punt 4 begrijpt waarom een afgeleide "doorgegeven" wordt naar eerdere stappen, heb je de kern.

## Zelftest

1. Wat betekent een afgeleide van 0 bij een functie als `3x² − 4x + 5`?
2. Waarom is `(f(x+h) − f(x)) / h` een benadering en geen exact antwoord?
3. Wat gebeurt er in gradient descent als de leersnelheid te groot is?
4. Leg de kettingregel uit aan iemand zonder wiskunde-achtergrond.
5. Waarom is de afgeleide nuttig voor het leren van een model?

<details>
<summary>Antwoorden</summary>

1. De helling is nul; daar zit een top of dal, hier het minimum.
2. `h` is klein maar niet nul; bij `h → 0` wordt de benadering exact.
3. De stappen schieten over het minimum heen en de waarde kan heen en weer springen of zelfs wegvliegen.
4. Als twee dingen achter elkaar de uitkomst veranderen, vermenigvuldig je hun veranderingssnelheden.
5. Hij vertelt per gewicht welke kant op en hoe sterk je moet bijsturen om de fout kleiner te maken.

</details>

## Afsluiten

```bash
git add -A
git commit -m "dag 5: afgeleiden, gradient descent en eerste deel micrograd"
git push
```

Logboekregel schrijven (wat begreep je, wat niet) en dag 5 afvinken.

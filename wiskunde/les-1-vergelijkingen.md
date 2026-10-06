# Les 1: variabelen en vergelijkingen oplossen (30 min)

Voor wie nog nooit algebra deed. Je kent het idee al: een variabele in code is een naam voor een waarde. Algebra gebruikt hetzelfde, alleen schrijf je het korter en los je ermee puzzels op.

## Stappenplan voor deze les

1. Lees de uitleg en reken de voorbeelden op papier mee (10 min).
2. Draai de codevoorbeelden en vergelijk (5 min).
3. Doe de 8 oefeningen **zonder** de uitwerkingen (12 min).
4. Controleer en markeer wat fout ging (3 min).

## 1. Variabelen en uitdrukkingen

Een **variabele** is een letter voor een getal die je nog niet weet of mag laten veranderen, net als `x = 5` in code.

Een **uitdrukking** combineert getallen en variabelen, zoals `3x + 2`. Als je een waarde invult, krijg je een getal:

```text
x = 5   →   3x + 2 = 3·5 + 2 = 17
x = 0   →   3x + 2 = 3·0 + 2 = 2
```

Let op: `3x` betekent `3 maal x`. Het malteken laat je in algebra vaak weg.

```python
x = 5
print(3 * x + 2)   # 17
```

## 2. Een vergelijking is een weegschaal

Een **vergelijking** zegt dat twee kanten gelijk zijn: `3x + 2 = 17`. **Oplossen** betekent uitzoeken welke `x` dat waar maakt.

Denk aan een weegschaal in balans. Wat je links doet, moet je ook rechts doen, anders raakt hij uit balans:

```text
3x + 2 = 17
3x + 2 − 2 = 17 − 2       (links en rechts 2 eraf)
3x = 15
3x / 3 = 15 / 3           (links en rechts delen door 3)
x = 5
```

**Controleer altijd** door je antwoord terug te vullen: `3·5 + 2 = 17`. Klopt, dan is het goed. Deze gewoonte bespaart je veel fouten.

De bewerkingen draai je om:

| Staat er... | Doe dan... |
| --- | --- |
| `+ 2` | trek 2 af |
| `− 2` | tel 2 op |
| `· 3` | deel door 3 |
| `/ 3` | vermenigvuldig met 3 |

Doe ze in omgekeerde volgorde als waarin de bewerkingen op `x` zijn uitgevoerd: eerst plus en min weghalen, dan pas vermenigvuldigen en delen.

## 3. Haakjes

`2(x + 3)` betekent: vermenigvuldig **alles** tussen de haakjes met 2.

```text
2(x + 3) = 2x + 6
```

Voorbeeld:

```text
2(x + 3) = 14
2x + 6 = 14
2x = 8
x = 4
```

Controle: `2(4 + 3) = 2·7 = 14`. ✓

Let op met een min-teken: `−2(x − 3) = −2x + 6`. Het min-teken geldt voor **beide** termen.

## 4. De variabele aan beide kanten

Soms staat `x` links én rechts. Haal alle `x`-termen naar één kant:

```text
5x − 4 = 2x + 8
5x − 2x − 4 = 8           (2x aan beide kanten eraf)
3x − 4 = 8
3x = 12                   (4 erbij)
x = 4
```

Controle: links `5·4 − 4 = 16`, rechts `2·4 + 8 = 16`. ✓

## 5. Breuken

Delen door een getal draai je om door te vermenigvuldigen:

```text
x / 4 = 3          →   x = 3 · 4 = 12
(x + 1) / 2 = 5    →   x + 1 = 10   →   x = 9
```

## 6. Formules omzetten

Een formule is een vergelijking met meer dan één variabele. Je kunt hem zo omzetten dat een andere variabele vrij staat:

```text
v = s / t       (snelheid = afstand gedeeld door tijd)
v · t = s       (beide kanten maal t)
s = v · t
```

Een voorbeeld uit jouw wereld: een model genereert `v` tokens per seconde. Dan is het aantal tokens in `t` seconden `v · t`.

## In code

Een vergelijking `ax + b = c` oplossen is gewoon stapsgewijs omkeren:

```python
def los_op(a: float, b: float, c: float) -> float:
    """Los a·x + b = c op."""
    return (c - b) / a


print(los_op(3, 2, 17))   # 5.0
print(los_op(2, 5, 19))   # 7.0
```

Dat de code één formule `(c − b) / a` is, komt uit dezelfde stappen als op papier: eerst `b` eraf, dan delen door `a`.

## Oefeningen

Fictieve prijzen bij opgave 7. Reken eerst op papier, controleer door in te vullen.

1. Los op: `2x + 5 = 19`
2. Los op: `4x − 3 = 21`
3. Los op: `3(x − 2) = 15`
4. Los op: `7x + 1 = 3x + 17`
5. Los op: `x/5 + 2 = 6`
6. Los op: `(2x − 1)/3 = 5`
7. Een API-call kost (fictief) 0,002 euro per 1.000 invoertokens en 0,010 euro per 1.000 uitvoertokens. Een call heeft 3.000 invoertokens en kost in totaal 0,026 euro. Hoeveel uitvoertokens waren het?
8. Een model genereert 450 tokens in 9 seconden. Wat is de snelheid `v` in tokens per seconde? Hoeveel tokens zijn dat in 40 seconden?

## Uitwerkingen

Kijk pas na een eerlijke poging.

<details>
<summary>Uitwerkingen</summary>

1. `2x = 14`, dus `x = 7`.
2. `4x = 24`, dus `x = 6`.
3. `x − 2 = 5`, dus `x = 7`. (Of: `3x − 6 = 15`, `3x = 21`, `x = 7`.)
4. `7x − 3x = 17 − 1`, `4x = 16`, dus `x = 4`.
5. `x/5 = 4`, dus `x = 20`.
6. `2x − 1 = 15`, `2x = 16`, dus `x = 8`.
7. Invoerkosten: 3 × 0,002 = 0,006. Rest: 0,026 − 0,006 = 0,020 euro voor uitvoer. Per 1.000 uitvoertokens 0,010, dus 2 × 1.000 = **2.000 uitvoertokens**.
8. `v = s/t = 450/9 = 50` tokens per seconde. In 40 seconden: `50 · 40 = 2.000` tokens.

</details>

## Wat je nu kunt

- Een eenvoudige vergelijking oplossen door de balans te bewaren.
- Haakjes uitwerken en breuken wegwerken.
- Een formule omzetten en controleren door in te vullen.

Fout gemaakt? Noteer het type opgave in je logboek (min-teken, haakjes, breuken) en doe er volgende week twee extra van.

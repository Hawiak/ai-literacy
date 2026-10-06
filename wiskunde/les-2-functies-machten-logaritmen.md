# Les 2: functies, machten en logaritmen (30 min)

Voor wie les 1 gedaan heeft. Deze les geeft je het idee van een **functie** en van een **helling**, de twee dingen die je zondag nodig hebt voor afgeleiden. Ook machten en logaritmen komen veel voor in AI: bijvoorbeeld bij het meten van een fout.

## Stappenplan voor deze les

1. Lees de uitleg en reken de voorbeelden op papier mee (10 min).
2. Draai de codevoorbeelden en vergelijk (5 min).
3. Doe de 8 oefeningen **zonder** de uitwerkingen (12 min).
4. Controleer en markeer wat fout ging (3 min).

## 1. Functies

Een **functie** is een regel die bij elke invoer precies één uitvoer geeft. In code kun je dat al:

```python
def f(x):
    return 2 * x + 1

print(f(3))   # 7
```

In algebra schrijf je `f(x) = 2x + 1`. Invullen: `f(3) = 2·3 + 1 = 7`.

## 2. Lineaire functies: de rechte lijn

`f(x) = a·x + b` heet **lineair**.

- `a` is de **helling**: hoeveel `f` stijgt als `x` met 1 toeneemt.
- `b` is de **beginwaarde**: de waarde van `f` bij `x = 0`.

Voorbeeld: een dienst kost 5 euro per maand vast plus 0,01 euro per call. Dan is `kosten(n) = 0,01·n + 5`. De helling 0,01 is de prijs per extra call.

**Helling uit twee punten.** Door `(x₁, y₁)` en `(x₂, y₂)`:

```text
a = (y₂ − y₁) / (x₂ − x₁)
```

Punten `(1, 3)` en `(4, 9)`: `a = (9 − 3)/(4 − 1) = 6/3 = 2`. Daarna `b` vinden door een punt in te vullen: `3 = 2·1 + b`, dus `b = 1`. De functie is `f(x) = 2x + 1`.

## 3. Machten en wortels

Een **macht** is herhaald vermenigvuldigen:

```text
x² = x · x           2³ = 2 · 2 · 2 = 8
x⁰ = 1               x⁻¹ = 1 / x
```

Rekenregels die je vaak nodig hebt:

```text
xᵃ · xᵇ = x^(a+b)      2³ · 2⁴ = 2⁷ = 128
(xᵃ)ᵇ = x^(a·b)        (2³)² = 2⁶ = 64
```

Een **wortel** is het omgekeerde van een macht: `√9 = 3` omdat `3² = 9`. Een wortel is ook een macht: `√x = x^(1/2)`.

```python
print(2**10)        # 1024
print(9 ** 0.5)     # 3.0
```

## 4. Een kromme: x²

Bij `f(x) = x²` is de grafiek een dal:

```text
x:   −3   −2   −1    0    1    2    3
f:    9    4    1    0    1    4    9
```

De functie daalt links van 0, is onderaan 0 en stijgt rechts. De **helling** verandert dus per punt: negatief links, nul onderaan, positief rechts. Zo'n dal is precies wat je bij het leren van een model wilt vinden: de plek waar de fout het kleinst is. De helling in elk punt heet de **afgeleide** en daarmee werk je zondag.

```python
for x in range(-3, 4):
    print(x, x**2)
```

Een tweede voorbeeld, `f(x) = x² − 4x`:

```text
x:   0    1    2    3    4
f:   0   −3   −4   −3    0
```

Het minimum zit bij `x = 2` (waarde −4).

## 5. Logaritmen in gewone woorden

Een **logaritme** is het omgekeerde van een macht. `2¹⁰ = 1024` betekent `log₂(1024) = 10`: "hoeveel keer moet ik 2 met zichzelf vermenigvuldigen om 1024 te krijgen?" Je kunt ook denken: hoe vaak verdubbelen?

```text
log₂(8)    = 3      want 2³ = 8
log₁₀(1000) = 3     want 10³ = 1000
```

```python
import math
print(math.log(8, 2))      # 3.0
print(math.log10(1000))    # 3.0
```

Twee dingen om te onthouden:

- Het getal `e ≈ 2,718` is een speciaal grondtal dat vaak voorkomt. `eˣ` en `ln(x)` (de natuurlijke logaritme) zijn elkaars omgekeerde. Je ziet ze vaak in formules voor kansen.
- Een logaritme maakt hele grote getallen hanteerbaar en zet vermenigvuldigen om in optellen: `log(a·b) = log(a) + log(b)`.

In AI gebruik je logaritmen bijvoorbeeld om een fout te meten: als een model een kans `p` aan het juiste antwoord geeft, is de fout `−log(p)`. Bij `p` dicht bij 1 is dat bijna 0, bij een kleine `p` groot. Daar kom je later op terug.

## Oefeningen

1. Gegeven `f(x) = 3x − 2`. Bereken `f(0)`, `f(4)` en `f(−1)`.
2. Een rechte lijn gaat door `(2, 5)` en `(6, 13)`. Bepaal de functie `f(x) = ax + b`.
3. Bereken `2⁵ · 2³` zonder rekenmachine als `2` tot een macht.
4. Bereken `(3²)³`.
5. Bereken `√49 + 4^(1/2)`.
6. Bereken `log₂(64)` en `log₁₀(1000)`.
7. Gegeven `f(x) = x² − 4x`. Bereken `f(0)`, `f(1)`, `f(2)`, `f(3)`, `f(4)`. Waar ligt het minimum?
8. Je begint met 1.000 tokens en verdubbelt het aantal steeds. Na hoeveel verdubbelingen heb je 1.024.000 tokens?

## Uitwerkingen

Kijk pas na een eerlijke poging.

<details>
<summary>Uitwerkingen</summary>

1. `f(0) = −2`, `f(4) = 3·4 − 2 = 10`, `f(−1) = −3 − 2 = −5`.
2. `a = (13 − 5)/(6 − 2) = 8/4 = 2`. Invullen bij `(2, 5)`: `5 = 2·2 + b`, dus `b = 1`. `f(x) = 2x + 1`. Controle met `(6, 13)`: `2·6 + 1 = 13`. ✓
3. `2⁵ · 2³ = 2⁸ = 256`.
4. `(3²)³ = 3⁶ = 729`.
5. `√49 = 7` en `4^(1/2) = 2`, samen 9.
6. `log₂(64) = 6` want `2⁶ = 64`. `log₁₀(1000) = 3`.
7. `f(0) = 0`, `f(1) = 1 − 4 = −3`, `f(2) = 4 − 8 = −4`, `f(3) = 9 − 12 = −3`, `f(4) = 16 − 16 = 0`. Het minimum is `−4` bij `x = 2`.
8. `1.000 · 2ⁿ = 1.024.000`, dus `2ⁿ = 1.024`, dus `n = 10` verdubbelingen.

</details>

## Wat je nu kunt

- Een functie lezen, invullen en de helling van een rechte lijn bepalen.
- Rekenen met machten en wortels, en een logaritme zien als het omgekeerde van een macht.
- Zien dat een kromme per punt een andere helling heeft. Daar bouwt zondag op.

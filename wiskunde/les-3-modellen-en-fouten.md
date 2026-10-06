# Les 3: modellen en fouten (30 min)

Voor wie les 1 en 2 gedaan heeft en zondag de afgeleide en gradient descent heeft gezien. Deze les laat zien dat "een model leren" neerkomt op een heel eenvoudige formule en een manier om de fout te meten. Dezelfde bouwstenen zitten in grote taalmodellen, alleen met miljarden getallen in plaats van twee.

## Stappenplan voor deze les

1. Lees de uitleg en reken de voorbeelden op papier mee (10 min).
2. Draai de codevoorbeelden en vergelijk (5 min).
3. Doe de 6 oefeningen **zonder** de uitwerkingen (12 min).
4. Controleer en markeer wat fout ging (3 min).

## 1. Een model is een formule met gewichten

Het eenvoudigste model: `ŷ = w·x + b` (spreek uit "y-hoed", de voorspelling).

- `x` is de invoer (bijvoorbeeld het aantal calls).
- `w` is het **gewicht**: hoeveel `x` meetelt (de helling).
- `b` is de **bias**: de beginwaarde (het snijpunt).
- `ŷ` is wat het model voorspelt. De werkelijke waarde noemen we `y`.

Met meer invoeren: `ŷ = w₁·x₁ + w₂·x₂ + b`. Bijvoorbeeld de prijs voorspellen uit oppervlakte en aantal kamers.

**Leren** betekent: de getallen `w` en `b` zo kiezen dat de voorspellingen goed zijn. Alle moderne modellen werken zo, alleen met veel meer gewichten.

## 2. Sommen en gemiddelden

`Σ` (sigma) betekent "tel op":

```text
Σ xᵢ  voor i = 1 tot n   =   x₁ + x₂ + ... + xₙ
```

Voor `[2, 4, 6, 8]` is de som 20 en het gemiddelde `20/4 = 5`.

```python
x = [2, 4, 6, 8]
print(sum(x), sum(x) / len(x))   # 20 5.0
```

## 3. Vectoren en het inproduct

Een **vector** is een lijst getallen, zoals `[1, 2, 3]`. Het **inproduct** van twee vectoren vermenigvuldigt ze paarsgewijs en telt dan op:

```text
[1, 2, 3] · [4, 5, 6] = 1·4 + 2·5 + 3·6 = 4 + 10 + 18 = 32
```

Het model met meer invoeren is dan: `ŷ = w · x + b`, met `w` en `x` als vectoren.

```python
w = [1, 2, 3]
x = [4, 5, 6]
print(sum(a * b for a, b in zip(w, x)))   # 32
```

Dit lijkt klein, maar vrijwel alles in een neuraal netwerk is zo'n inproduct, heel vaak achter elkaar uitgevoerd (een matrixvermenigvuldiging is een tabel van inproducten).

## 4. De fout meten: loss

Hoe goed is een model? Vergelijk voorspelling `ŷ` met de echte `y`:

```text
fout = ŷ − y
```

Fouten kunnen positief of negatief zijn en heffen elkaar dan op. Daarom kwadrateer je ze en neem je het gemiddelde. Dat heet de **gemiddelde kwadratische fout** (MSE, mean squared error):

```text
MSE = ( (ŷ₁ − y₁)² + (ŷ₂ − y₂)² + ... ) / n
```

Voorbeeld met data `(x, y)`: `(1, 3)`, `(2, 5)`, `(3, 7)`.

- Model `ŷ = 2x + 1` geeft voorspellingen 3, 5, 7. Alle fouten zijn 0, dus MSE = 0.
- Model `ŷ = 2x` geeft 2, 4, 6. Fouten −1, −1, −1, kwadraten 1, 1, 1, MSE = 1.

De **loss** is zo'n getal: hoe kleiner, hoe beter het model past. Leren = de gewichten kiezen waarbij de loss het kleinst is.

## 5. De loss als dal

Houd `b` vast en laat alleen `w` variëren. De loss als functie van `w` is een dal, net als `x²` uit les 2: er is een `w` waarbij de loss minimaal is. Daar is de **helling van de loss nul**, en dat is precies wat zondag besproken is. Gradient descent loopt stap voor stap naar die bodem toe door tegen de helling in te bewegen.

## In code

```python
data = [(1, 2), (2, 4), (3, 6)]   # echte relatie: y = 2x


def mse(w: float) -> float:
    fouten = [(w * x - y) ** 2 for x, y in data]
    return sum(fouten) / len(fouten)


for w in [0, 1, 2, 3, 4]:
    print(f"w={w}  mse={mse(w):.2f}")
```

Verwachte uitvoer:

```text
w=0  mse=18.67
w=1  mse=4.67
w=2  mse=0.00
w=3  mse=4.67
w=4  mse=18.67
```

Je ziet het dal, met het minimum bij `w = 2`. Probeer ook `w = 1.5` en `w = 2.5`. Past dit bij wat je zondag zag met `x² − 4x`?

## Oefeningen

1. Gegeven `y = 3x₁ + 2x₂ − 1` met `x₁ = 2` en `x₂ = 5`. Bereken `y`.
2. Bereken de som en het gemiddelde van `[2, 4, 6, 8]`.
3. Bereken het inproduct `[2, 0, −1] · [3, 5, 4]`.
4. Data `(1, 2)`, `(2, 4)`, `(3, 6)` en model `ŷ = 3x`. Bereken de MSE.
5. Zelfde data, model `ŷ = 2x`. Wat is de MSE?
6. Programmeeropdracht: schrijf `mse(w)` uit de code hierboven na en probeer `w = 1.5` en `w = 2.5`. Welke waarde is lager, en waarom ligt het tussen de waarden hierboven?

## Uitwerkingen

Kijk pas na een eerlijke poging.

<details>
<summary>Uitwerkingen</summary>

1. `3·2 + 2·5 − 1 = 6 + 10 − 1 = 15`.
2. Som 20, gemiddelde 5.
3. `2·3 + 0·5 + (−1)·4 = 6 + 0 − 4 = 2`.
4. Voorspellingen 3, 6, 9. Fouten `3−2 = 1`, `6−4 = 2`, `9−6 = 3`. Kwadraten 1, 4, 9. Som 14, MSE = `14/3 ≈ 4,67`.
5. Voorspellingen 2, 4, 6 gelijk aan `y`, dus MSE = 0.
6. Bij `w = 1,5` zijn de fouten `−0,5·x`: kwadraten `0,25·(1+4+9) = 3,5`, MSE `3,5/3 ≈ 1,17`. Bij `w = 2,5` is het hetzelfde: `1,17`. Beide liggen tussen 0 (bij `w = 2`) en 4,67 (bij `w = 1` en `w = 3`), dus op het dal tussen die waarden.

</details>

## Wat je nu kunt

- Een eenvoudig model opschrijven als `ŷ = w·x + b` en uitrekenen.
- De fout van een model meten met MSE en uitleggen waarom je kwadrateert.
- Uitleggen dat "leren" betekent: de gewichten kiezen waarbij de loss klein is, met de afgeleide als kompas.

Dit is een miniatuur van het idee achter een taalmodel: **hetzelfde principe**, alleen op veel grotere schaal en met andere functies. Dat maakt de rest van het jaar een stuk minder mysterieus.

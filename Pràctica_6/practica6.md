# PRÀCTICA 6 - Introducció als bucles en Python

En aquesta pràctica aprendrem a utilitzar els bucles `while` i `for`.

## Introducció

Hi ha dues estructures primitives de Python per programar bucles i són el `while` i el `for`.

## Bucle `while`

Un bucle `while` executa un bloc de codi quan la condició és `true`.

### Sintaxi `while`

```python
while <condició>:
    # codi a executar
```

```python
i = 0

while i < 10:
    print(i)
    i = i + 1
```

### `break` statement

Amb el `break` podem parar el bucle tot i que la condició continui sent certa:

```python
i = 1 

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

### `continue` statement

Amb el `continue` podem aturar la iteració actual i saltar a la següent.

```python
i = 1 

while i < 6:
    print(i)
    if i == 3:
        continue
    i += 1
```

### `else` statement

Amb l'`else` podem executar un bloc de codi, un cop la condició ja no sigui certa:

```python
i = 1 

while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')
```

### Exercicis bucle `while`

Fes els [exercicis](./exercicis.md) 1 i 2.

## Bucle `for`

Un bucle `for` s'utilitza per iterar sobre una sèrie d'elements (com una llista o un rang de números).

### Sintaxi del `for`

```python
for <element> in <seqüència>:
    # codi a executar
```

```python
fruits = ['apple', 'orange', 'cherry']

for fruit in fruits:
    print(fruit)
```

### Exercicis bucle `for`

Fes els [exercicis](./exercicis.md) 3, 4, i 5.

## Funció `range()` i bucles `for`

La funció `range()` és molt útil quan treballem amb bucles, ja que ens permet generar seqüències de números per iterar-hi fàcilment. Aquesta funció s’utilitza amb molta freqüència dins dels bucles `for` per definir el nombre d'iteracions o per controlar el rang de valors que volem recórrer.

La sintaxi de `range()` és la següent:

```python
range(inici, fi, pas)
```

Cada paràmetre té un significat específic:

1. **inici** (opcional): És el valor des d'on comença la seqüència. Per defecte és `0`.
2. **fi** (obligatori): És el valor fins al qual arriba la seqüència, però **no s'inclou en el rang**.
3. **pas** (opcional): És el salt entre els valors successius de la seqüència. El valor per defecte és `1`.

### Exemples d'ús de `range()`

#### 1. Usar `range()` amb un únic argument

Quan `range()` té només un argument, aquest indica el **valor de finalització**, mentre que l'inici per defecte serà `0`, i el pas serà `1`.

```python
for i in range(5):
    print(i)
```

**Sortida**:

```bash
0
1
2
3
4
```

En aquest exemple, `range(5)` genera els números `0` fins a `4`, ja que `5` és el valor de finalització i no s'inclou en el rang.

#### 2. Usar `range()` amb dos arguments

Quan `range()` té dos arguments, el primer argument defineix el **valor d'inici**, i el segon, el **valor de finalització** (sense incloure’l en el rang).

```python
for i in range(2, 7):
    print(i)
```

**Sortida**:

```bash
2
3
4
5
6
```

En aquest exemple, `range(2, 7)` genera els valors de `2` fins a `6`.

#### 3. Usar `range()` amb tres arguments

Quan `range()` té tres arguments, el primer defineix l’**inici**, el segon la **finalització** (sense incloure’l en el rang) i el tercer el **pas** (o salt).

```python
for i in range(1, 10, 2):
    print(i)
```

**Sortida**:

```bash
1
3
5
7
9
```

En aquest cas, `range(1, 10, 2)` genera els números de `1` fins a `9`, amb un salt de `2` entre cada valor.

#### 4. Rang en ordre descendent

Podem utilitzar `range()` per crear un rang en ordre descendent, simplement indicant un pas negatiu.

```python
for i in range(10, 0, -2):
    print(i)
```

**Sortida**:

```bash
10
8
6
4
2
```

Aquí, `range(10, 0, -2)` comença des de `10` i decreix fins a `2`, amb un salt de `-2`.

### Exercicis funció `range()` i bucles `for`

Fes els [exercicis](./exercicis.md) 6 i 7.

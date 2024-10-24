# PRÀCTICA 6 -  Introducció als bucles en Python

En aquesta pràctica aprendrem a utilitzar els bucles `while` i `for`.

## Introducció

Escriure

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

## Exercici 1: Comptar fins a 50

Crea un programa que utilitzi un bucle `while` per imprimir els números del 1 al 50.

## Exercici 2: Sumar fins a un nombre

Crea un programa que demani a l'usuari un nombre i utilitzi un bucle `while` per sumar els números de 1 fins a aquell nombre. Mostra el resultat final.

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

## Exercici 3: Iterar sobre una llista

Crea una llista amb els noms de 5 fruites i utilitza un bucle `for` per imprimir cada fruita.

```python
fruits = ['maduixa', 'plàtan', 'poma', 'kiwi', 'taronja']
```

## Exercici 4: Taula de multiplicar

Crea un programa que demani a l'usuari un número i utilitzi un bucle `for` per imprimir la taula de multiplicar d'aquest número (del 1 al 10).

## Exercici 5: Sumar elements d'una llista

Crea una llista amb números enters. Utilitza un bucle `for` per sumar tots els números de la llista i imprimir el resultat.

## Exercici 6: Contar elements

Crea una llista amb alguns noms. Utilitza un bucle `for` per comptar quants noms hi ha en la llista i imprimeix el resultat.

## Exercici 7: Sumar números fins que l'usuari vulgui

Crea un programa que utilitzi un bucle `while` per permetre a l'usuari introduir números fins que introdueixi un `0`. Al final, imprimeix la suma total dels números introduïts.

## Exercici 8: Mostrar llista de la compra

Crea un programa que permeti a l'usuari introduir elements en una llista de la compra. Utilitza un bucle `while` perquè l'usuari pugui continuar introduïnt elements fins que escrigui `fi`. Al final, mostra la llista de la compra.

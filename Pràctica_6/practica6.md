# PRÀCTICA 6 -  Introducció als bucles en Python

ESBORRANY.

## Objectius

- Entendre i utilitzar els bucles `while` i `for`.
- Aplicar els bucles en situacions reals per resoldre problemes simples.

## Continguts

### Bucles `while`

Un bucle `while` executa un bloc de codi mentre una condició sigui verdadera.

### Sintaxi `while`

```python
while <condició>:
    # codi a executar
```

### Exercici 1: Comptar fins a 10

Crea un programa que utilitzi un bucle `while` per imprimir els números del 1 al 10.

**Exemple de solució:**

```python
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
```

### Exercici 2: Sumar fins a un nombre

Crea un programa que demani a l'usuari un nombre i utilitzi un bucle `while` per sumar els números de 1 fins a aquell nombre. Mostra el resultat final.

**Exemple de solució:**

```python
num = int(input("Introdueix un nombre: "))
suma = 0
contador = 1

while contador <= num:
    suma += contador
    contador += 1

print("La suma dels números de 1 a", num, "és:", suma)
```

---

### Bucles `for`

Un bucle `for` s'utilitza per iterar sobre una sèrie d'elements (com una llista o un rang de números).

### Sintaxi del `for`

```python
for <element> in <seqüència>:
    # codi a executar
```

### Exercici 3: Iterar sobre una llista

Crea una llista amb els noms de 5 fruits i utilitza un bucle `for` per imprimir cada fruit.

**Exemple de solució:**

```python
fruits = ['maduixa', 'plàtan', 'poma', 'kiwi', 'taronga']
for fruit in fruits:
    print(fruit)
```

### Exercici 4: Taula de multiplicar

Crea un programa que demani a l'usuari un número i utilitzi un bucle `for` per imprimir la taula de multiplicar d'aquest número (del 1 al 10).

**Exemple de solució:**

```python
num = int(input("Introdueix un número per veure la seva taula de multiplicar: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

---

### Exercici 5: Sumar elements d'una llista

Crea una llista amb números enteros. Utilitza un bucle `for` per sumar tots els números de la llista i imprimir el resultat.

**Exemple de solució:**

```python
numeros = [2, 4, 6, 8, 10]
suma = 0

for num in numeros:
    suma += num

print("La suma dels números de la llista és:", suma)
```

---

### Exercici 6: Contar elements

Crea una llista amb alguns noms. Utilitza un bucle `for` per comptar quants noms hi ha en la llista i imprimeix el resultat.

**Exemple de solució:**

```python
noms = ['Anna', 'Jordi', 'Laura', 'Marc', 'Sara']
contador_noms = 0

for nom in noms:
    contador_noms += 1

print("Hi ha", contador_noms, "noms a la llista.")
```

---

### Exercici 7: Sumar números fins que l'usuari vulgui

Crea un programa que utilitzi un bucle `while` per permetre a l'usuari introduir números fins que introdueixi un `0`. Al final, imprimeix la suma total dels números introduïts.

**Exemple de solució:**

```python
suma = 0
num = None

while num != 0:
    num = int(input("Introdueix un número (0 per acabar): "))
    suma += num

print("La suma total és:", suma)
```

### Exercici 8: Mostrar llista de la compra

Crea un programa que permeti a l'usuari introduir elements en una llista de la compra. Utilitza un bucle `while` perquè l'usuari pugui continuar introduint elements fins que escrigui `fi`. Al final, mostra la llista de la compra.

**Exemple de solució:**

```python
llista_compra = []
element = ""

while element.lower() != "fi":
    element = input("Introdueix un element per la llista de la compra (escriu 'fi' per acabar): ")
    if element.lower() != "fi":
        llista_compra.append(element)

print("La llista de la compra és:", llista_compra)
```

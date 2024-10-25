# PRÀCTICA 6 - Exercicis

## Bucle `while`

### Exercici 1: Comptar fins a 50

Crea un programa que utilitzi un bucle `while` per imprimir els números del 1 al 50.

### Exercici 2: Sumar fins a un nombre

Crea un programa que demani a l'usuari un nombre i utilitzi un bucle `while` per sumar els números de 1 fins a aquell nombre. Mostra el resultat final.

## Bucle `for`

### Exercici 3: Iterar sobre una llista

Crea una llista amb els noms de 5 fruites i utilitza un bucle `for` per imprimir cada fruita.

```python
fruites = ['maduixa', 'plàtan', 'poma', 'kiwi', 'taronja']
```

### Exercici 4: Sumar elements d'una llista

Crea una llista amb números enters. Utilitza un bucle `for` per sumar tots els números de la llista i imprimir el resultat.

### Exercici 5: Contar elements

Crea una llista amb alguns noms. Fes que estigui ordenada i utilitza un bucle `for` per imprimir els noms com una llista numerada.

Exemple:

```bash
1. Anna
2. Berta
3. Carla
...
```

## Funció `range()` i bucles `for`

### Exercici 6: Taula de multiplicar

Crea un programa que demani a l'usuari un número i utilitzi un bucle `for` per imprimir la taula de multiplicar d'aquest número (del 1 al 10).

#### Exemple de sortida

Si l'usuari introdueix el número `5`, el programa mostrarà:

```bash
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

#### Indicacions ex 6

- Pots utilitzar `range()` per recórrer els números de l'1 al 10 dins del bucle `for`.
- Recorda que dins del bucle pots multiplicar el número introduït per cada valor del `range(1, 11)` per obtenir el resultat correcte en cada línia de la taula.

### Exercici 7: Números Parells fins a un Nombre Determinat

Escriu un programa que demani a l’usuari un número sencer positiu `n` i, després, mostri tots els números parells des de `0` fins a `n` (incloent `n` si aquest és parell).

#### Exemple d'execució

```bash
Introdueix un número sencer positiu: 10
0
2
4
6
8
10
```

#### Indicacions ex 7

- Utilitza un bucle `for` juntament amb `range()` per recórrer els números des de `0` fins a `n`.
- Recorda que `range(inici, fi, pas)` et permet saltar cada dos números.
- Prova amb diferents valors de `n` per veure com funciona.

## Practiquem

### Exercici 8: Sumar números fins que l'usuari vulgui

Crea un programa que utilitzi un bucle `while` per permetre a l'usuari introduir números fins que introdueixi un `0`. Al final, imprimeix la suma total dels números introduïts.

### Exercici 9: Comptar elements superiors a un valor donat

Crea una llista amb diferents números enters positius i negatius. A continuació, demana a l'usuari un valor de referència (també enter) i utilitza un bucle `for` per comptar quants elements de la llista són més grans que aquest valor. Al final, mostra el nombre d’elements que compleixen la condició.

### Exercici 10: Llista de la compra

Recuperant l'exercici 12 de la [pràctica 5](/Pràctica_5/practica5.md), utilitza el bucle `while` per tal de millorar la funcionalitat del programa anterior.

Crea un programa que permeti a l'usuari gestionar la seva llista de la compra fins que decideixi sortir. El programa ha de tenir les següents funcionalitats:

1. **Afegir un element**: Si l'usuari introdueix `1`, se li demanarà que indiqui el nom d'un article per afegir a la llista de la compra. Si l'element ja existeix a la llista, el programa ha de mostrar el missatge **"Aquest element ja està a la llista."**; si no, ha de mostrar **"Element afegit a la llista."**.

2. **Eliminar un element**: Si l'usuari introdueix `2`, se li demanarà que indiqui el nom d'un article per eliminar de la llista de la compra. Si l'element no està a la llista, el programa ha de mostrar el missatge **"Aquest element no està a la llista."**; si s'elimina correctament, ha de mostrar **"Element eliminat de la llista."**.

3. **Mostrar la llista**: Si l'usuari introdueix `3`, el programa ha de mostrar la llista actual de la compra.

4. **Sortir del programa**: Si l'usuari introdueix `0`, el programa ha de finalitzar.

5. **Missatge d'error**: Si l'usuari introdueix una opció diferent de les esmentades, el programa ha de mostrar el missatge **"Opció no vàlida."**.

L'usuari veurà les opcions abans de cada acció.

Llista inicial de la compra:

```python
# Llista inicial de la compra
llista_compra = [
    'suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs',
    'pasta de dents', 'pa', 'llet', 'ous', 'tomàquets', 'formatge'
]
```

#### Exemple del programa

```bash
Opcions:
1. Afegir un element a la llista de la compra
2. Eliminar un element de la llista de la compra
3. Mostrar la llista de la compra
0. Sortir
Escull una opció (0, 1, 2 o 3): 1
Escriu el nom de l'element que vols afegir: cafè
Element afegit a la llista.

Opcions:
1. Afegir un element a la llista de la compra
2. Eliminar un element de la llista de la compra
3. Mostrar la llista de la compra
0. Sortir
Escull una opció (0, 1, 2 o 3): 3
Llista de la compra actual:
['suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs', 'pasta de dents', 'pa', 'llet', 'ous', 'tomàquets', 'formatge', 'cafè']
```

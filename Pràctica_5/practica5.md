# PRÀCTICA 5 - Llistes

En aquesta pràctica coneixerem com es fan llistes en Python. A més, també introduim la funció `input()`.

## Preparació

Dins de `practiques-1-trim-el_teu_nom` crea una carpeta anomanda `Pràctica_5`. Aquí anirem creant els arxius d'aquesta pràctica.

## Introducció

Les llistes s'utilitzen per guardar múltiples elements en una sola variable.

Són unes de els 4 "build-in" tipus de dades de Python que serveixen per emmagatzemar múltiples elements. Les altres tres serien: les "tuples", els "sets" i els "diccionaris".

Les llsites es creen utilitzant claudàtors `[]`:

```python
thislist = ['apple', 'banana', 'cherry']
print(thislist)
```

## Característiques

### Elements de la llista

Els elements de la llista estan ordenats i la llista accepta valors duplicats.

Exemples:

```python
llista_a = ['apple', 'banana', 'cherry']
llista_b = ['banana', 'apple', 'cherry']
llista_c = ['apple', 'cherry', 'cherry']

# La llista_a NO és igual a la llista_b, en una apple és el primer element i en l'altre no.

# La llista_c és correcta: en el primer element hi tenim apple, en el segon cherry i en el tercer també cherry.
```

Per canviar l'ordre dels elements de les llistes ho podem fer manualment, més endavant ho veurem, o a partir de mètodes de les llistes, que també ja els anirem introduïnt.

### Accedim als elements

Per accedir als elements de les llistes farem `nom_llista[<índex>]`.

Provem:

```python
llista_a = ['apple', 'banana', 'cherry']
print(llista_a[1])
```

Què obtens?

Fixa't que l'indexació comença per 0, o sigui:

- llista_a[0] retornarà `apple`
- llista_a[1] retornarà `banana`
- llista_a[2] retornarà `cherry`

### Llargada de la llista

Tal com hem vist amb els Strings utilitzem la funció `len()`

```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

### Tipus de dades dels elements

La llistes poden ser de qualsevol tipus de dades i també poden contenir diferents tipus de dades en una sola llista.

```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["cat", 7, True, "female"]
```

### Creació de llistes

Les llistes es poden crear a partir de la propia creació de la variable llista o a partir de la funció `list`.

```python
new_list1 = ["apple", "banana", "cherry"]
new_list2 = [] # Llista buida que ja omplirem
new_list3 = list(("apple", "banana", "cherry")) # Fixa't que hi ha doble parèntesis
```

### Elements de les llistes

Per comprovar si un element està o no dins d'una llista utilitzarem `in`.

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

## Indexació de les llistes

Anteriorment ja hem vist una petita introducció de com accedim als elements.

Per accedir als elements de les llistes fem `nom_llista[<índex>]` on el primer element té `índex = 0`

Veiem una mica més a fons.

### Negative Indexing

Negative indexing means start from the end

`-1` refers to the last item, `-2` refers to the second last item etc.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```

### Rang dels índexs

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a **new list** with the specified items. You can store this new list into a new variable.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

new_list = thislist[1:3]
print(new_list)
```

També podem utilitzar aquesta altra sintaxis si volem tots els elements del principi fins a un cert índex o tots els elements del final a partir d'un índex concret:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[:4])
print(thislist[4:])
```

## Modificar elements

### Canviar un element

To change the value of a specific item, refer to the index number:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "watermelon"
print(thislist)
```

Podeu trobar més especificacions de modificar elements [aquí](https://www.w3schools.com/python/python_lists_change.asp).

### Inserir elements

To insert a new list item, without replacing any of the existing values, we can use the `insert()` method.

The `insert()` method inserts an item at the specified index:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```

## Exercici 1

A partir de els següents llistes fes que `llista1` contingui `['Estudio', 'primer', 'de', 'batxillerat']`. Fes print de l'estat inicial de les dues llistes i de l'estat final de `llista1`.

```python
llista1 = ['primer', 'hola', 'batxillerat']
llista2 = ['Estudio', 'de', 'casa']
```

## Afegir elements

### Append

To add an item **to the end of the list**, use the `append()` method:

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

### Insert

To insert a list item **at a specified index**, use the `insert()` method.

The `insert()` method inserts an item at the specified index:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

### Extend

To append elements **from another list to the current list**, use the `extend()` method.

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(tropical)
print(thislist)
```

Another way to join two lists is by using the + operator.

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```

## Exercici 2

Fes print de l'estat inicial de la `llista_compra`. Després afegeix `maduixes` al final de la `llista_compra` i `patates` a la tercera posició. Fes print de l'estat final de la llista.

```python
llista_compra = ['suc de taronja', 'cereals', 'pastanagues', 'cebes']
```

## Exercici 3

Crea dues llistes. Una que contingui el nom dels primers 6 mesos de l'any i l'altre, els altres sis. Posteriorment, crea una tercera llista composta per tots els mesos de l'any. Fes print per pantalla de les tres llistes.

## Eliminar elements

### Remove Specified Item

The `remove()` method removes the specified item.

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

If there are more than one item with the specified value, the `remove()` method removes the first occurrence:

```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
```

### Remove Specified Index

The `pop()` method removes the specified index. Using `pop()`, the removed item can be stored to another variable.

```python
thislist = ["apple", "banana", "cherry"]
my_item = thislist.pop(1)
print(thislist)
print(my_item)
```

If you do not specify the index, the `pop()` method removes the last item.

```python
thislist = ["apple", "banana", "cherry"]
my_item = thislist.pop()
print(thislist)
print(my_item)
```

### Using del

The `del` keyword also removes the specified index. It's not commonly used.

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```

The `del` keyword can also delete the list completely.

```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

### Clear the list

The `clear()` method empties the list.

The list still remains, but it has no content.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```

## Exercici 4

Fes print de l'estat inicial de la `llista_compra`. Després:

1. Elimina l'últim element i guarda'l en la variaible `comprar_mes_tard`. Fes print de la `llista_compra` i de `comprar_mes_tard`.
2. Elimina les `maduixes` de la `llista_compra`. Fes print de la `llista_compra`.
3. Elimina el segon element de la `llista_compra`. Fes print de la `llista_compra`.
4. Buida `llista_compra`. Fes print de la `llista_compra`.

```python
llista_compra = ['suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs', 'pasta de dents']
```

## Més funcions i mètodes

Igual que el `len()` existeixen altres funcions "build-in" que ens permeten sumar, trobar el màxim i el mínim d'una llista formada per nombres: `sum()`, `max()` i `min()`.

```python
thislist = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
print(sum(thislist))
print(max(thislist))
print(min(thislist))
```

Pel que fa mètodes útils de les llistes, podeu consultar [aquí](https://www.w3schools.com/python/python_lists_methods.asp).

Font: [W3S](https://www.w3schools.com/python/python_lists.asp)

## Exercici 5

Busca un mètode en el link de l'apartat anterior per ordenar alfabèticament la `llista_compra`. Mostra per pantalla l'abans i el després de la llista.

```python
llista_compra = ['suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs', 'pasta de dents']
```

## Exercici 6

Busca un mètode en el link de l'apartat anterior que et retorni el nombre de `cereals` que hi ha a la `llista_compra`. Mostra per pantalla la llista i després la frase `Cereals apareix <num_cereals> vegades a la llista de la compra.`

```python
llista_compra = [
    'suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs',
    'pasta de dents', 'pa', 'llet', 'ous', 'tomàquets', 'cereals', 'formatge', 
    'iogurt', 'patates', 'arròs', 'cereals', 'pollastre', 'peix', 'llimones', 
    'aigua', 'cereals', 'gelat', 'sucre', 'llenties', 'cereals', 'pernil', 
    'plàtans', 'cereals', 'xocolata'
]
```

## Capturar dades de l'usuari amb `input()`

En Python, la funció `input()` es fa servir per capturar dades que l'usuari introdueix a través del teclat. Aquesta funció retorna sempre una cadena de text (tipus `str`), independentment del que l'usuari introdueixi.

### Com funciona?

Quan utilitzem `input()`, el programa s'atura i espera que l'usuari escrigui alguna cosa. Després de prémer la tecla **Enter**, el valor introduït es guarda a la variable que hem especificat.

### Exemples

```python
nom = input("Com et dius? ")
print(f"Hola, {nom}!")
```

```python
edat = input("Quants anys tens? ")
edat = int(edat)  # Convertim la cadena a enter
print(f"Tens {edat} anys.")
```

### Errors comuns amb `input()`

Un error comú és oblidar-se de convertir el resultat de `input()` quan volem treballar amb nombres. Si intentem fer operacions matemàtiques amb una cadena de text, Python donarà un error.

Per exemple:

```python
edat = input("Quants anys tens? ")
print(edat + 5)  # Això donarà error, ja que 'edat' és un text, no un nombre!
```

## Exercici 7

Fes un programa que permeti afegir un article a la llista de la compra, però només si aquest article no hi és. Fes servir una condició `if-else`.

1. Demana a l'usuari un article a afegir amb la funció `input()`.
2. Comprova si l'article està ja a la `llista_compra`.
3. Si l'article no està a la llista, afegeix-lo amb el mètode `append()`.
4. Si ja hi és, mostra un missatge indicant que l'article ja està present.

```python
llista_compra = [
    'suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs',
    'pasta de dents', 'pa', 'llet', 'ous', 'tomàquets', 'cereals', 'formatge'
]
```

## Exercici 8

Millorem el programa anterior.Fes un programa que permeti afegir un article a la llista de la compra només si:

- L'article no existeix ja a la llista.
- L'article no és una cadena buida (`""`) o una cadena que només contingui espais.

Fes servir operadors lògics `and` i `not` per implementar aquestes condicions.

Instruccions:

1. Demana a l'usuari que introdueixi un article a afegir a la `llista_compra` utilitzant `input()`.
2. Comprova si l'article **no** està a la llista **i** l'article **no** és una cadena buida o només espais.
3. Si compleix amb aquestes condicions, afegeix-lo a la llista.
4. Si alguna de les condicions no es compleix, mostra un missatge explicatiu.

```python
llista_compra = [
    'suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs',
    'pasta de dents', 'pa', 'llet', 'ous', 'tomàquets', 'cereals', 'formatge'
]
```

## Exercici 9

Dissenya un programa que comprovi si pots comprar els articles de la llista de la compra amb un pressupost limitat. Cada article té un preu associat. El programa ha de sumar els preus dels articles i determinar si pots comprar-los tots amb el pressupost donat.

1. Calcula el cost total dels articles utilitzant `if-else` i `sum()`.
2. Fes print d'un missatge indicant si pots permetre't la compra o no.

```python
llista_compra = ['suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes']
preus = [2.5, 4.0, 3.0, 1.2, 1.5]  # preu de cada article a la llista
pressupost = 10  # Pressupost disponible
```

## Exercici 10

L'usuari ha de comprar un component electrònic d'una llista donada. 

```python
# Llista d'elements i preus
components = ["Portàtil gaming", "Targeta gràfica RTX 4090", "Monitor 4K", "Disc SSD 2TB", "Processador Intel i9"]
preus = [1500, 2000, 800, 250, 600]
```

El programa:

1. Mostra una llista de components electrònics disponibles.
2. Demana a l'usuari el seu pressupost.
3. Demana a l'usuari quin component vol comprar.
4. El programa comprova si el component existeix.
5. El programa comprova si l'usuari té prou pressupost per comprar el component i fa la compra si és possible.

Cal retornar els missatges corresponents.

## Exercici 11

En el formulari d'inscripció d'una pàgina web els usuaris han d'entrar la seva data de naixement seguint el següent format: `08/12/2000`, on el primer nombre és el dia, el segon el mes i el tercer l'any.

Crea la variable anomenada `date` i demana a l'usuari que introdueixi una data.

Després, fes que el programa et retorni, segons les indicacions anteriors:

- **"Data correcta."** si la data introduïda segueix el format `dd/mm/aaaa`.
- **"Eps! Aquesta data no és correcta! Recorda que el format és dd/mm/aaaa."** si la data no segueix aquest format.

Et pot ser útil el següent mètode dels Strings: `.split()`, que et permet dividir una cadena de text en una llista de parts utilitzant un delimitador com, per exemple, la barra `/`.

### Exercici 12

Crea un programa que permeti a l'usuari gestionar la seva llista de la compra. El programa ha de tenir les següents funcionalitats:

1. **Afegir un element**: Si l'usuari introdueix `1`, se li demanarà que indiqui el nom d'un article per afegir a la llista de la compra. Si l'element ja existeix a la llista, el programa ha de mostrar el missatge **"Aquest element ja està a la llista."**; si no, ha de mostrar **"Element afegit a la llista."**.

2. **Eliminar un element**: Si l'usuari introdueix `2`, se li demanarà que indiqui el nom d'un article per eliminar de la llista de la compra. Si l'element no està a la llista, el programa ha de mostrar el missatge **"Aquest element no està a la llista."**; si s'elimina correctament, ha de mostrar **"Element eliminat de la llista."**.

3. **Mostrar la llista**: Si l'usuari introdueix `3`, el programa ha de mostrar la llista actual de la compra.

4. **Missatge d'error**: Si l'usuari introdueix una opció diferent a les tres anteriors, el programa ha de mostrar la llista **"Opció no vàlida."**.

Cal mostrar les opcions que té l'usuari abans de demanar que introdueixi 1, 2 o 3.

```python
llista_compra = [
    'suc de taronja', 'maduixes', 'cereals', 'pastanagues', 'cebes', 'espinacs',
    'pasta de dents', 'pa', 'llet', 'ous', 'tomàquets', 'cereals', 'formatge'
]
```

## Per tancar la pràctica

A més, crea un fitxer `.md` en la pràctica 5 i copia els enunciats dels exercicis. En aquest fitxer crea links per poder accedir als fitxers `.py` des de l'enunciat corresponent. Per exemple amb una frase tipus:

> Accedeix a la resolució d'aquest exercici clicant aquí.

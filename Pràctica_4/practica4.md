# PRÀCTICA 4 - Noves estructures de programació

En aquesta pràctica coneixerem noves estructures de programació i la seva sintaxis en Python.

## Prepara`ció

Crea un nou repositori de GitHub anomenat `practiques-1-trim-el_teu_nom` (sense cognoms). Configuració:

- Privat
- Crea automàticament el README
- La resta d'opcions deixa-les en la configuració per default

Un cop creat, vés a `Settings > Collaborators > Add people > 'Mar-PVV'`.

Clona aquest repositori dins de la teva carpeta `Programació`. Dins de `practiques-1-trim-el_teu_nom` crea una carpeta anomanda `Pràctica_4`. Aquí anirem creant els arxius d'aquesta pràctica.

## Python If ... Else

### Introducció

En la programació tenen una gran utilitat els condicionals normalment anomenats "If - Else". Veiem un exemple amb llenguatge natural:

```bash
plou = Veritat

si plou:
    Agafar el paraigües.
si no:
    No agafar el paraigües.
```

Veiem com seria amb Python:

```python
plou = True

if plou:
    print("Agafo el paraigües.")
else:
    print("No cal agafar el paraigües.")
```

### Python Indentation

Per tal de que el programa "entri" dins del `print("Agafo el paraigües.")` o l'altra opció, s'ha de posar l'indentation (espais en blanc al principi de la línia). Aquesta indentation la fem utilitzant la tecla `Tab` del nostre teclat, la que té una / dues fletxes sobre el `Bloq Maj`.

Fes la prova sense aquesta indentaton:

```python
plou = True

if plou:
print("Agafo el paraigües.")

else:
print("No cal agafar el paraigües.")
```

### Logic Conditions

S'ha de tenir en compte que l'`<statement>` o condició, en el cas de l'exemple el `plou`, ha de ser una condició lògica, o sigui que el seu resultat sigui o `True` o `False`.

Anem a veuren algunes des de l'IDLE del Python:

#### Numèriques

```python
# Equals
9 == 9
9 == 0

# Not equals
9 != 0
9 != 9

# Greater than
4 > 5
5 > 4

# Less than or equal to
1 <= 1
1 <= 9
9 <= 1
```

Una mica el resum:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

#### Altres tipus de condicions

Anem a provar amb els Strings. A l'IDLE:

```python
name = 'Carla'
'e' in name
'car' in name
'Car' in name
'Hola' == name
'Carla' == name 
```

Entre moltes d'altres que anirem treballant o que podem aconseguir a través de mètodes i funcions.

### Exercici 1

Crea un fitxer Python anomenat `exercici_1` dins de la carpeta `Pràctica_4`. Per aquest exercici necessitarem una funció que ens genera nombres random i que la trobem al mòdul `random`. Per això al principi del fitxer posem:

```python
import random
```

Més informació sobre el mòdul `random` [aquí](https://www.geeksforgeeks.org/random-numbers-in-python/).

En aquest document crea les següents variables:

```python
num_1 = random.randint(1, 10) # Random integer between 1 and 10 (inclusive)
num_2 = random.randint(1, 10)
name = 'Pere Vives'
```

Aquest exercici tindrà dos blocs `If-Else`:

- El primer: ha de comparar els dos nombres i mostrar per pantalla `<num_gran> és més gran que <num_petit>`
- El segon: ha de comparar el nombre de lletres de `name`, sense comptar l'espai (més informació més avall), amb el `num_1` i mostrar per pantalla `<nom> té <més/menys> de <num_1> lletres.`.

Per tal de descomptar l'espai, recorda que tenim el mètode dels Strings anomenat `name.count(<String a comptar>)` que et permetrà comtpar quants espais té dins la variable `name`.

Un cop et funcioni, guarda l'arxiu i actualitza el repositori al GitHub utilitzant les comandes de Git corresponents.

Anem a continuar amb més detalls sobre l'`If-Else`. Font [W3S](https://www.w3schools.com/python/python_conditions.asp).

### Elif

The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

### Short Hand If

If you have only one statement to execute, you can put it on the same line as the if statement.

```python
if a > b: print("a is greater than b")
```

### Short Hand If ... Else

If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

```python
a = 2
b = 330
print("A") if a > b else print("B")
```

### Logical operators

Els operadors lògics ens permetran itereccionar entre diferents statements. Anem a veure un exemple amb llenguatge natural:

```bash
plou = Veritat
he_de_sortir = Fals

si plou i he_de_sortir:
    Agafar el paraigües.
si no: # si no plou o si no he de sortir
    No agafar el paraigües.
```

Veiem-ne un altre:

```bash
porto_targeta = Veritat
porto_efectiu = Fals

si porto_targeta o porto_efectiu:
    Puc fer el pagament.
si no: # si no porto ni efectiu ni targeta
    No puc fer el pagament.
```

Veiem-los tots:

#### And - i

The `and` keyword is a logical operator, and is used to combine conditional statements:

```python
# Example 1
if 200 > 33 and 500 > 200:
    print("Both conditions are True")

# Example 2
if 33 > 200 and 500 > 200:
    print("Both conditions are True")
else:
    print("One or both conditions are not True")
```

#### Or - o

The `or` keyword is a logical operator, and is used to combine conditional statements:

```python
# Example 1
if 33 > 200 or 500 > 200:
    print("At least one of the conditions is True")

# Example 2
if 33 > 200 or 200 > 500:
    print("At least one of the conditions is True")
else:
    print("Both conditions are False")
```

#### Not - no

The `not` keyword is a logical operator, and is used to reverse the result of the conditional statement:

```python
# Example 1
plou = True

if not plou:
    print("No està plovent")
else:
    print("Plou")

# Example 2
num_1 = 33
num_2 = 200
if not num_1 > num_2:
    print(num_1 + " no és més gran que " + num_2)
```

#### Nested If

You can have `if` statements inside `if` statements, this is called nested if statements.

```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```

#### The pass Statement

`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

```python
a = 33
b = 200

if b > a:
  pass
```

### Exercici 2

Tenim la següent llista de preus:

1. Llibreta 3€
2. Llapis 1,50€
3. Pack de retoladors 3,50€
4. Calculadora 23€
5. Estoig 8€

Crea una variable a partir del generador random d'integers que et retorni un número enter de l'1 al 5 (inclosos). A partir de combinacions de `If-Else` fes que es mostri per pantalla `El producte seleccionat costa <preu>€.`

### Exercici 3

Genera dos nombres random que puguin anar del -10 al 10. Fes que el programa et retorni si:

- Els dos nombres són positius
- Els dos nombres són negatius
- Els dos nombres són zero
- Si n'hi ha un de cada (un positiu i un negatiu)
- Si un és positiu i l'altre un zero.
- Si un és negatiu i l'altre un zero.

### Exercici 4

Genera un nombre aleatori del 0 al 5000. Fes que et retorni si el nombre generat seria un any de traspàs. El missatge final seria: `L'any <any> és/no és any de traspàs.`.

### Exercici 5

Genera un nombre aleatori del 1 al 12, interpretant els mesos de l'any. Fes que et retorni quants dies té aquest mes: `El mes número <num_mes> té <num_dies> dies.`

### Exercici 6

Genera 3 nombres aleatoris del 1 al 100. Cadascun d'aquests tres nombres representa els costats d'un triangle. Fes que el programa retorni si és un triangle equilàter, isòsceles o escalé. Fes que també et digui si es tracta d'un triangle rectangle.

### Exercici 7

Crea les següents dues variables: 

```python
toca_programacio = bool(random.randint(0,1))
ordinador_carregat = bool(random.randint(0,1))
```

Segons les condicions fes que retorni:

- Tot correcte!
- Falta de material.

### Exercici 8

Crea les següents dues variables: 

```python
anem_viatge = bool(random.randint(0,1))
entre_setmana = bool(random.randint(0,1))
```

Segons les condicions fes que retorni:

- Posar alarma a les 7h
- Desacivar alarma

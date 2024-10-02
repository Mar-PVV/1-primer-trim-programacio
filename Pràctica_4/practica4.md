# PRÀCTICA 4 - Noves estructures de programació

En aquesta pràctica coneixerem noves estructures de programació i la seva sintaxis en Python.

## Preparaicó

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

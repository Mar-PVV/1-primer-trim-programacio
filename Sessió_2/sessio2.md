# SESSIÓ 2 - First steps amb Python

En aquesta sessió instal·larem i farem la primera presa de contacte amb el llenguatge de programació Python.

## Instal·lació

Segueix les indicacions de la professora.

## Hello World

When learning a new programming language, it is customary to start with an "hello world" example. As simple as it is, this one line of code will ensure that we know how to print a string in output and how to execute code within cells in a notebook.

1. Crea una carpeta dins de Programació anomenada `Sessió_2`.
2. Crea un fitxer amb el següent contingut i guarda'l com a `hello_world.py`.
3. Des de la consola ves a la carpeta `Sessió_2` i executa el programa.

Codi del fitxer `hello_world.py`:

```python
print('Hello World!')
```

Executa el programa:

```bash
python .\hello_world.py
```

## Python IDLE

Per tal de no haver d'executar cada vegada el programa, per fer petits tests utilitzarem l'IDLE (Integrated Development and Learning Enviroment), consola que executa cada línia de codi que anem entrant.

1. Obre l'IDLE de Python.
2. Escriu `print('Hello World!')` i observa què apareix.

## Variables i tipus

### Variables

S’utilitzen per emmagatzemar informació a la memòria.

Les variables s ́on espais a la memòria als qual hi donem un nom per fer-les servir al llarg del codi.

En python no cal declarar variables (reservar espai a la memòria abans de fer-les servir), simplement podem fer:

```python
x = 2
nom = 'Mar'
preu = 2.54
love_maths = True
```

### Tipus bàsics d'objectes (build in)

Existeixen diferents tipus de variables segons el que s’hi vulgui guardar. Els tipus de variables més bàsics són:

- Variables enteres (per nombre enters): `x = 2`. Python pot treballar amb tants dígits com calgui amb variable enteres.
- Punt flotant (float, nombres amb decimals): `x = 2.0`. Processió doble.
- String: variable amb caràcters (text). S'escriu entre cometes simples o dobles (depenent l'estil).
- Booleà: variables que poden prendre el valor "cert" (`True`) o "fals" (`False`). S’utilitzen sobretot per controlar esdeveniments (while’s o if ’s).

Python detecta sol quin tipus de variables s’està declarant segons el que se li està assignant.

> Atenció
> En cap cas podrem operar amb variables de diferents tipus.

Observem els tipus de variable a partir de la funció integrada `type()`:

```python
type(x)
type(nom)
type(preu)
type(love_maths)
type(23.5)
type('hello')
```

### Canviar el tipus de les variables

Busca les funcions integrades per els següents canvis de variables:

- Integer to float
- Float to integer      Què passa en aquest cas?
- Strings to integers or floats
- Integers or floats to strings

Anem a provar el següent pels Booleans:
```python
# Convert True to int
int(True)
```

```python
# Convert 1 to boolean
bool(1)
```

```python
# Convert 0 to boolean
bool(0)
```

```python
# Convert True to float
float(True)
```

Què n'extreus?

> Observa que quan s'escriu darrere d'un # en Python no s'executa el que hi posa. Serveix per escriure comentaris.

## Operacions bàsiques amb nombres i variables

### Operacions bàsiques amb nombres 

Operacions bàsiques amb nombres:
```python
# Addition operation expression
43 + 60 + 16 + 41

# Subtraction operation expression
50 - 60

# Multiplication operation expression
5 * 5

# Division operation expression
25 / 5
25 / 6

# Integer division operation expression
25 // 5
25 // 6

# Modulus
25 % 5
25 % 6 
```

### Operacions i variables

Ara juguem amb les operacions i les variables.

Dins de `Sessió_2` crea un nou fitxer `hores_a_segons.py`.

Aquest programa tindrà dues variables: una que representa les hores i una altra que representa els segons. A partir d'un nombre 'hores donades, per exemple 120 hores, calcula quants segons són i fes que mostri per pantalla el resultat utilitzant la funció `print()`.

> IMPORTANT! El nom de les variables ha de ser representatiu. No posem `asdf = 120`.

Ara, podem millorar el nostre programa mostrant per pantalla una mica més d'informació a partir del `print()`. Dins d'aquesta funció podem mostrar text i també variables. Per exemple:

```python
num_hores = 120
num_minuts = num_hores * 60
print(num_hores + ' hores són ' + num_minuts + ' minuts.')
```

### Crear noves variables o sobreescriure

Observa i prova:

```python
# Store value into variable
x = 43 + 60 + 16 + 41

# Print out the value in variable
x


# Use another variable to store the result of the operation between variable and value
y = x / 60
y

# Overwrite variable with new value
x = x / 60
x
```

## Strings

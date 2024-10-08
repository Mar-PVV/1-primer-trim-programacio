# PRÀCTICA 2 - First steps amb Python

En aquesta pràctica instal·larem i farem la primera presa de contacte amb el llenguatge de programació Python.

## Instal·lació

Segueix les indicacions de la professora.

## Hello World

When learning a new programming language, it is customary to start with an "hello world" example. As simple as it is, this one line of code will ensure that we know how to print a string in output and how to execute code within cells in a notebook.

1. Crea una carpeta dins de Programació anomenada `Pràctica_2`.
2. Crea un fitxer amb el següent contingut i guarda'l com a `hello_world.py`.
3. Des de la consola ves a la carpeta `Pràctica_2` i executa el programa.

Codi del fitxer `hello_world.py`:

```python
print('Hello World!')
```

Executa el programa:

```bash
py hello_world.py
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

### Exercicis 1

De la següent pàgina [web](https://www.w3schools.com/python/python_exercises.asp) completa els exericis següents:

- Get Started
- Comments
- Variables
- Variable Names
- Multiple Variable Values
- Output Variable
- Data Types

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

Dins de `Pràctica_2` crea un nou fitxer `hores_a_segons.py`.

Aquest programa tindrà dues variables: una que representa les hores i una altra que representa els segons. A partir d'un nombre 'hores donades, per exemple 120 hores, calcula quants segons són i fes que mostri per pantalla el resultat utilitzant la funció `print()`.

> IMPORTANT! El nom de les variables ha de ser representatiu. No posem `asdf = 120`.

Ara, podem millorar el nostre programa mostrant per pantalla una mica més d'informació a partir del `print()`. Dins d'aquesta funció podem mostrar text i també variables. Per exemple:

```python
num_hores = 120
num_minuts = num_hores * 60
print(num_hores + ' hores són ' + num_minuts + ' minuts.')
```

Ara per provar, ves a la consola a la carpeta corresponent i prova:

```bash
py hores_a_segons.py
```

Quin error et surt? Com ho arreglaries?

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

### Exercicis 2

De la següent pàgina [web](https://www.w3schools.com/python/python_exercises.asp) completa els exericis següents:

- Numbers
- Casting

## Strings

### Informació bàsica

The following example shows a string contained within 2 quotation marks:

```python
# Use quotation marks for defining string
"Pere Vives"
```

We can also use single quotation marks:

```python
# Use single quotation marks for defining string
'Pere Vives'
```

A string can be a combination of spaces and digits:

```python
# Digitals and spaces in string
'1 2 3 4 5 6 '
```

A string can also be a combination of special characters:

```python
# Special characters in string
'@#2_#]&*^%$'
```

We can print our string using the print statement:

```python
# Print the string
print("hello!")
```

We can bind or assign a string to another variable:

```python
# Assign string to variable
Name = "Pere Vives"
Name
```

### Indexació

Anem a accedir a un sol caràcter del string:

```python
print(Name[1])
```

Què observes?

Ara prova...

```python
print(Name[15])
```

Què passa?

Per saber com de llarg és un string podem fer:

```python
len(Name)
```

Ara anem a imprimir només una part de l'string:

```python
# Take the slice on variable Name with only index 0 to index 3
Name[0:4]

# Take the slice on variable Name with only index 8 to index 11
Name[8:12]
```

### Concatenar

We can concatenate or combine strings by using the addition symbols, and the result is a new string that is a combination of both:

```python
# Concatenate two strings
Statement = Name + "is the best"
Statement
```

To replicate values of a string we simply multiply the string by the number of times we would like to replicate it. In this case, the number is three. The result is a new string, and this new string consists of three copies of the original string:

```python
# Print the string for 3 times
3 * "Pere Vives"
```

You can create a new string by setting it to the original variable. Concatenated with a new string, the result is a new string that changes from Pere Vives to "Pere Vives is the best".

```python
# Concatenate strings
Name = "Pere Vives"
Name = Name + " is the best"
Name
```

### Escape Sequences

Back slashes represent the beginning of escape sequences. Escape sequences represent strings that may be difficult to input. For example, back slash "n" represents a new line. The output is given by a new line after the back slash "n" is encountered:

```python
# New line escape sequence
print("Pere Vives \n is the best" )
```

Similarly, back slash "t" represents a tab:

```python
# Tab escape sequence
print("Pere Vives \t is the best" )
```

If you want to place a back slash in your string, use a double back slash:

```python
# Include back slash in string
print("Pere Vives \\ is the best" )
```

We can also place an "r" before the string to display the backslash:

```python
# r will tell python that string will be display as raw string
print(r" Pere Vives \ is the best" )
```

### String Operations

There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the data.

Let's try with the method `upper`; this method converts lower case characters to upper case characters:

```python
# Convert all the characters in string to upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)

B = A.upper()
print("After upper:", B)
```

The method replace replaces a segment of the string, i.e. a substring with a new string. We input the part of the string we would like to change. The second argument is what we would like to exchange the segment with, and the result is a new string with the segment changed:

```python
# Replace the old substring with the new target substring is the segment has been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B
```

The method find finds a sub-string. The argument is the substring you would like to find, and the output is the first index of the sequence. We can find the sub-string jack or el.

```python
# Find the substring in the string. Only the index of the first elment of substring in string will be the output
Name = "Michael Jackson"
Name.find('el')

# Find the substring in the string.
Name.find('Jack')
```

If the sub-string is not in the string then the output is a negative one. For example, the string 'Jasdfasdasdf' is not a substring:

```python
# If cannot find the substring in the string
Name.find('Jasdfasdasdf')
```

### Exercicis 3

De la següent pàgina [web](https://www.w3schools.com/python/python_exercises.asp) completa els exericis següents:

- Tots els de Strings

## Pràctica

### Juguem amb nombres

Crea un document dins de `Pràctica_2` anomenat `nombres.py`.
Donats tres nombres naturals d'una xifra (els que tu vulguis), fes que el programa mostri per pantalla tots els nombres de 2 xifres que es poden crear a partir d'aquests tres nombres (es poden repetir).

Exemple de la sortida del programa:

> Tinc els nombres 2, 5 i 7. Amb ells puc crear X nombres diferents de dues xifres:
>
> El 22, 25, 27, 52, ...

### De segons a dies

Crea un document dins de `Pràctica_2` anomenat `segons_a_dies.py`.
Crea la variable `segons = 278718`. Fes que el programa mostri per pantalla quants dies, hores, minuts i segons són.

### Jocs amb una paraula

Crea un document dins de `Pràctica_2` anomenat `paraula.py`.
Crea una variable que sigui `paraula` i assigna-li qualsevol paraula de 5 lletres que vulguis en minúscula.

Un cop tinguis aquesta paraula, utilitzant els mètodes mostrats i altres que pots trobar [aquí](https://www.w3schools.com/python/python_strings.asp), fes que el teu programa retorni:

- El nombre de lletres que té la paraula
- Les dues primeres llertes de la paraula
- Les dues últimes
- La paraula amb la primera lletra majúscula
- La paraula tota amb majúscula
- La paraula repetida 5 vegades
- La paraula més un espai i el teu nom

### Juguem amb un conte

Crea un document dins de `Pràctica_2` anomenat `conte.py`.
Crea la variable següent:

```python
conte = """Vet aquí una vegada, als afores d’un poble molt petit situat ben amunt de la muntanya, hi vivia la família d’una nena. A la nena li agradava molt posar-se un abric vermell amb caputxa que li havia fet la seva àvia. Encara que no fes gota de fred ella sempre volia posar-se la caputxa. És per això que per aquelles contrades li deien La Caputxeta Vermella.

La Caputxeta era una nena alegre. Com totes les nenes tenia moments per tot, però generalment era riallera i divertida. Cada dimecres acompanyava a la seva mare al mercat a comprar fruites i verdures per casa. Aquell mateix dia abans que es fes fosc, les dues creuaven el bosc per visitar a la seva àvia que estava malalta i portar-li algunes provisions del mercat.

Un dia, en tornar del mercat, la mare de La Caputxeta no es trobava massa bé i va dir-li que no anirien a casa l’àvia aquella tarda. L’àvia vivia sola en una casa al mig del bosc i com que en aquella època no tenien telèfons la Caputxeta va pensar que si no anava ningú a visitar-la, potser es preocuparia."""
```

Fitxa't que els strings que ocupen múltiples línies s'han d'emmarcar entre tres dobles cometes `"""`.

Un cop tens el conte copiat, consultant els diferents [mètodes dels Strings](https://www.w3schools.com/python/python_strings_methods.asp), fes que el programa retorni:

- El text inicial
- Quants caràcters té el text
- Quantes vegades apareix `Caputxeta` al text
- El text des de l'inici fins el primer cop que surt Caputxeta (sense retallar el text sinó amb mètodes de Strings)
- El text canviant `Caputxeta` per `Caputxa` (a partir de mètodes de Strings)

### Entrega

Entrega al Classroom els fitxers creats dins la carpeta `Pràctica_2`.

## Pàgines útils de Python

Guardeu-les per tenir-les accessibles.

- [W3 Schools](https://www.w3schools.com/python/python_intro.asp)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)

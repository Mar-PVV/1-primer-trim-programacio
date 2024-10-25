# PRÀCTICA 7 - Funcions

En aquesta pràctica aprendrem què són les funcions en Python, com definir-les i com utilitzar-les en els nostres programes. Les funcions són una manera d'organitzar el codi en blocs que poden ser reutilitzats i que faciliten la resolució de problemes de manera estructurada.

## Què és una Funció?

Una funció és un bloc de codi amb un nom que realitza una tasca específica. Es pot cridar o executar la funció en qualsevol moment simplement utilitzant el seu nom. Les funcions ens ajuden a:

- Organitzar el codi en blocs.
- Evitar la repetició de codi.
- Fer que el codi sigui més fàcil de llegir i mantenir.
  
## Sintaxi Bàsica

Una funció en Python es defineix amb la paraula clau `def`, seguida del nom de la funció i parèntesis. Aquí tens la sintaxi general:

```python
def nom_de_la_funcio():
    # Codi de la funció
    # Les línies que comencen amb espais dins la funció són el "bloc de codi"
    # que es durà a terme quan es cridi a aquesta funció
    ...
```

### Exemple senzill de funció sense paràmetres

```python
def saludar():
    print("Hola, benvingut a l'aprenentatge de Python!")

# Cridem a la funció
saludar()
```

En aquest exemple, hem creat una funció anomenada `saludar` que, quan és cridada, mostra el missatge "Hola, benvingut a l'aprenentatge de Python!".

## Paràmetres de les funcions

Les funcions poden tenir paràmetres, que són variables que la funció necessita per fer la seva tasca. Els paràmetres es passen entre els parèntesis de la funció quan la definim.

```python
def saludar(nom):
    print("Hola, " + nom + "!")

# Cridem a la funció amb un valor per al paràmetre
saludar("Carla")
```

Aquí, el paràmetre `nom` és una variable que es passa a la funció, i quan la cridem, li donem el valor `"Carla"`. Això farà que el programa mostri el missatge: `Hola, Carla!`.

## Valors de Retorn

Les funcions també poden "retornar" un valor al programa amb la paraula clau `return`. Això és útil quan volem que la funció realitzi un càlcul i ens retorni el resultat.

```python
def suma(a, b):
    resultat = a + b
    return resultat

# Podem guardar el resultat en una variable
res = suma(3, 5)
print(res)  # Mostra 8
```

Quan una funció retorna un valor, podem guardar-lo en una variable o utilitzar-lo directament en altres càlculs.

## Exercicis bàsics

### Exercici 1: Càlcul de l'àrea d'un Rectangle

Escriu una funció anomenada `area_rectangle` que calculi i retorni l'àrea d'un rectangle, donades la seva amplada i la seva alçada com a paràmetres.

```python
def area_rectangle(amplada, alçada):
    # Calcula l'àrea i retorna el valor
    pass

# Exemple d'ús
area = area_rectangle(5, 3)
print("L'àrea és:", area)  # Ha de mostrar "L'àrea és: 15"
```

### Exercici 2: Informació personal

Crea una funció anomenada `mostrar_info` que prengui com a paràmetre el nom d'una persona, la seva data de naixement i la seva edat. Aquesta informació l'ha de demanar a l'usuari. La funció ha d'imprimir per pantalla aquesta informació seguint el patró de l'exemple.

Exemple:

```bash
Nom: Pere Vives
Data naixement: 20 de gener de 1858
Edat: 166 anys
```

```python
def mostrar_info(nom, dia, mes, any, edat):
    # Completa la funció per mostrar la informació corresponent
    pass  # Aquest `pass` es pot eliminar un cop hagis completat la funció
```

### Exercici 3: Funció per verificar si un número és parell

Defineix una funció `es_parell` que prengui un número com a paràmetre i retorni `True` si el número és parell, o `False` si és senar.

```python
def es_parell(numero):
    # Retorna True si el número és parell, False si és senar
    pass

# Exemple d'ús
print(es_parell(4))  # Ha de mostrar True
print(es_parell(7))  # Ha de mostrar False
```

## Exercicis més complerts

### Exercici 4: Càlcul dels divisors d'un nombre

Escriu una funció anomenada `divisors` que prengui un número enter com a paràmetre i retorni una llista amb tots els divisors d'aquest número.

1. Utilitza un bucle `for` per comprovar cada número entre 1 i el número donat (inclusiu).
2. Utilitza una condició `if` per verificar si el número és divisor del nombre donat (és a dir, si el residu de la divisió és zero).
3. Si és divisor, afegeix-lo a la llista de divisors.
4. Retorna la llista al final.

```python
def divisors(num):
    # Escriu el codi aquí
    pass

# Exemple d'ús
print(divisors(12))  # Ha de mostrar [1, 2, 3, 4, 6, 12]
```

### Exercici 5: Comprovació de nombres primers

Crea una funció anomenada `es_primer` que prengui un número enter com a paràmetre i retorni `True` si el número és primer, o `False` en cas contrari.

1. La funció ha de verificar si el número és menor que 2, en aquest cas retorna `False`.
2. Utilitza un bucle `for` per comprovar si el número té divisors entre 2 i la seva arrel quadrada.
3. Si el número té algun divisor en aquest interval, retorna `False`.
4. Si no té divisors, retorna `True`.

```python
import math

def es_primer(num):
    # Escriu el codi aquí
    pass

# Exemple d'ús
print(es_primer(7))   # Ha de mostrar True
print(es_primer(10))  # Ha de mostrar False
```

### Exercici 6: Resolució d'equacions de segon grau

Escriu una funció anomenada `resoldre_equacio_segongrau` que prengui els coeficients `a`, `b`, i `c` d'una equació de segon grau de la forma `ax^2 + bx + c = 0` i retorni una llista amb les possibles solucions.

1. Calcula el discriminant `d = b^2 - 4ac`.
2. Si el discriminant és positiu, calcula les dues solucions i retorna-les.
3. Si el discriminant és zero, retorna una única solució.
4. Si el discriminant és negatiu, retorna `None` per indicar que no hi ha solucions reals.

```python
import math

def resoldre_equacio_segongrau(a, b, c):
    # Escriu el codi aquí
    pass

# Exemple d'ús
print(resoldre_equacio_segongrau(1, -3, 2))  # Ha de mostrar [2.0, 1.0]
print(resoldre_equacio_segongrau(1, 2, 1))   # Ha de mostrar [-1.0,]
print(resoldre_equacio_segongrau(1, 0, 1))   # Ha de mostrar None
```

### Exercici 7: Progressió aritmètica

Crea un programa que generi una progressió aritmètica segons els paràmetres indicats per l'usuari. El programa ha de demanar a l'usuari el primer terme de la progressió, la diferència (diferència constant entre termes consecutius) i el nombre total de termes que vol imprimir per pantalla.

1. Defineix una funció anomenada `progressio_aritmetica` que prengui tres paràmetres:
   - `primer_terme`: el valor inicial de la progressió.
   - `dif`: la diferència constant entre termes.
   - `n_termes`: el nombre total de termes que es volen generar.

2. La funció ha de retornar una llista amb els `n_termes` de la progressió.

3. La funció utilitzarà un bucle `for` per calcular els termes successius de la progressió sumant la diferència al terme anterior.

4. Després, el programa ha de mostrar la llista completa de la progressió generada.

#### Exemple de la sortida ex 7

```bash
Introdueix el primer terme de la progressió: 3
Introdueix la diferència de la progressió: 5
Introdueix el nombre de termes a generar: 4
La progressió aritmètica és: [3, 8, 13, 18]
```

### Exercici 8: Successió de Fibonacci

Crea un programa que generi la Successió de Fibonacci segons els paràmetres indicats per l'usuari. El programa ha de demanar a l'usuari els dos primers termes de la successió i el nombre total de termes que vol imprimir per pantalla.

1. Defineix una funció anomenada `successio_fibonacci` que prengui tres paràmetres:
   - `terme_1`: primer terme de la successió.
   - `terme_2`: segon terme de la successió.
   - `n_termes`: el nombre total de termes que es volen generar.

2. La funció ha de retornar una llista amb els `n_termes` de la successió.

3. La funció utilitzarà un bucle `for` per calcular els termes successius de la successió sumant els dos termes anteriors.

4. Després, el programa ha de mostrar la llista completa de la successió.

#### Exemple de la sortida ex 8

```bash
Introdueix el primer terme de la successió: 0
Introdueix la diferència de la successió: 3
Introdueix el nombre de termes a generar: 6
La progressió aritmètica és: [0, 3, 3, 6, 9, 15]
```

### Exercici 9: Càlcul del Mínim Comú Múltiple (mcm)

Crea un programa que permeti a l'usuari calcular el mínim comú múltiple (mcm) de dos nombres enters positius. El programa ha de seguir els següents passos:

1. Demanar a l'usuari que introdueixi dos nombres enters positius.
2. Definir una funció anomenada `calcular_mcm` que accepti aquests dos nombres com a arguments.
3. Calcular el mcm.
4. Retornar el valor del mcm i mostrar-lo a l'usuari.

Assegura't de validar que els nombres introduïts són positius abans de fer el càlcul.

L'usuari podrà anar calculant el mcm de diferents nombres fins que introdueixi `fi` i el tanqui el programa.

### Exercici 10: Millorem la llista de la compra

Copia la resolució de l'exercici 10 de la [pràctica 6](/Pràctica_6/exercicis.md) (o 11 si vas fer l'ampliació) i millora el codi per tal de que quedi més net i ordenat utilitzant les funcions.

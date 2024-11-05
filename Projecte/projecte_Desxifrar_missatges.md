# Desxifrat de missatges

## Objectiu

Desenvolupar un programa que analitzi textos xifrats amb el xifratge Cèsar, basats en els missatges enviats pels nazis amb les màquines Enigma. El programa ha de ser capaç de trobar la clau de xifrat utilitzada en el xifrat de César i desxifrar els missatges, mostrant el text original.

## Funcionalitats a implementar

### Analitzar el text d'entrada

El programa ha de permetre a l'usuari introduir el missatge xifrat.

Per un programa més complert, l'usuari introdueix el nom del fitxer `.txt` que conté el missatge xifrat. Aquest fitxer ha d'estar guardat en la carpeta `files` de dins del projecte.

### Determinar la clau de xifrat

El programa ha de detectar i determinar automàticament la clau de xifrat utilitzada per al xifrat de César mitjançant la tècnica que trii l'usuari:

- Tècniques d'anàlisi de freqüència (els missatges són en anglès).
- Comparant amb possibles textos clars (presència de la previsió meteorològica en tots els textos).

### Desxifrar el missatge

Un cop trobada la clau de xifrat, el programa ha de desxifrar el missatge i mostrar el text original de manera clara i llegible.

### Mostrar els resultats

El programa ha de mostrar tant la clau de xifrat trobada com el text desxifrat a l'usuari.

### Guardar els missatges xifrats

A l'acabar de desxifrar un missatge, ha de generar un informe `.txt` a la carpeta `results` on aparegui:

- Títol: Missatge desxifrat
- Data i hora de quan s'ha desxifrat el missatge
- Missatge original
- Missatge desxifrat
- Clau cèsar utilitzada i tipus de tècnica utilitzada

### Sortir del programa

L'usuari ha de poder sortir del programa quan ho requereixi, si l'usuari no ho indica el programa ha de proposar desxifrar un altre text. Si l'usuari indica que vol sortir, aquest mostrarà un missatge de comiat i finalitzarà l'execució.

## A tenir en compte

- El programa ha de ser amigable i proporcionar retroalimentació clara a l'usuari.
- Us pot ser útil consultar com es llegeixen i creen documents `.txt`. Consulteu [aquí](https://www.w3schools.com/python/python_file_handling.asp).
- Us pot ser útil l'ús de [diccionaris](https://www.w3schools.com/python/python_dictionaries.asp).

## Enllaços d'interès

- [Documentació](./Documentació.md) del projecte
- [Avaluació](./Avaluació.md) del projecte

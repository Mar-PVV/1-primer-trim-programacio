# Aplicació Gestor de tasques

## Objectiu

Desenvolupar un Gestor de Tasques que permeti a l'usuari crear, organitzar i gestionar les seves tasques diàries de manera eficaç. El programa ha de permetre afegir tasques amb dates límit, marcar-les com a completades i oferir diferents opcions per visualitzar-les.

## Funcionalitats a implementar

### Afegir una tasca

Permetre a l'usuari afegir una nova tasca amb un títol, descripció i data límit. Assegura't que el format de la data sigui correcte i que no es pugui afegir una tasca amb una data passada.

### Visualitzar totes les tasques

Mostrar una llista de totes les tasques afegides, incloent el títol, la descripció, la data límit i l'estat (completada o no). Les tasques completades es mostren al final de la llista. Les tasques en que la data límit ja hagi passat s'han de comprar d'un color diferent (més informació [aquí](https://sentry.io/answers/print-colored-text-to-terminal-with-python/)).

### Marcar tasca com a completada

Permetre a l'usuari marcar una tasca específica com a completada, actualitzant el seu estat.

### Eliminar una tasca

Permetre a l'usuari eliminar una tasca.

### Actualitzar data límit

Permetre a l'usuari editar la datat límit d'una tasca.

### Mostrar tasques d'avui

Permetre a l'usuari visualitzar només les tasques que tenen la data límit igual a la data actual.

### Ordenar tasques

Per defecte les tasques estan ordenades tal com s'han anat afegit. Tot i això, l'usuari pot ordenar una tasca indicant la posició específica.

### Sortir del programa

L'usuari ha de poder sortir del programa quan ho requereixi, si l'usuari no ho indica el programa ha de continuar proposant quina acció vol fer a continuació l'usuari. Si l'usuari indica que vol sortir, aquest mostrarà un missatge de comiat i finalitzarà l'execució.

## A tenir en compte

- El programa ha de ser amigable i proporcionar retroalimentació clara a l'usuari.
- Us pot ser útil l'ús de [diccionaris](https://www.w3schools.com/python/python_dictionaries.asp).

## Enllaços d'interès

- [Documentació](./Documentació.md) del projecte
- [Avaluació](./Avaluació.md) del projecte

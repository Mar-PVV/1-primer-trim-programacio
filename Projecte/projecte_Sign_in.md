# Sign In d'una aplicació

## Objectiu

El vostre projecte consisteix a desenvolupar la funcionalitat de sign in per a una aplicació. Aquesta funcionalitat permetrà als nous usuaris crear un compte introduint el seu nom d'usuari, contrasenya i data de naixement, mentre es garanteix que es compleixin determinades condicions i requisits de seguretat.

## Funcionalitats a implementar

### Introducció del nom d'usuari

- L'usuari ha de poder introduir un nom d'usuari.
- Comprovar que el nom d'usuari no coincideixi amb els noms d'usuaris ja creats:
  - `usuari1`
  - `marta23`
  - `joan2023`
  - `alex.smith`
  - `carla`
- Si el nom d'usuari ja existeix, s'ha de mostrar un missatge d'error indicant que l'usuari ha de triar un altre nom.
- El nom d'usuari no pot contenir espais.

### Creació de la contrasenya

- L'usuari ha de crear una contrasenya.
- Sol·licitar que la contrasenya es torni a introduir per verificar que coincideix amb la primera entrada.
- Comprovar que la contrasenya compleix els següents requisits bàsics:
  - Ha de tenir almenys 8 caràcters.
  - Ha de contenir almenys una lletra majúscula.
  - Ha de contenir almenys una lletra minúscula.
  - Ha de contenir almenys un número.
  - Ha de contenir almenys un caràcter especial (@, #, $, &).
- Mostrar un missatge d'error si la contrasenya no compleix algun dels requisits.

### Introducció de la data de naixement

- L'usuari ha de poder introduir la seva data de naixement en el format **dd/mm/aaaa**.
- Comprovar que el format és correcte.
- Verificar que l'usuari té 16 anys o més. Si l'usuari no compleix aquesta condició, s'ha de mostrar un missatge d'error.

### Sortir del programa

L'usuari ha de poder sortir del programa quan ho requereixi, si l'usuari no ho indica el programa ha de proposar si l'usuari vol introduir un altre usuari. Si l'usuari indica que vol sortir, aquest mostrarà un missatge de comiat i finalitzarà l'execució.

## A tenir en compte

El programa ha de ser amigable i proporcionar retroalimentació clara a l'usuari en cada pas del procés de registre.

## Enllaços d'interès

- [Documentació](./Documentació.md) del projecte
- [Avaluació](./Avaluació.md) del projecte

# Aplicació gestor de contactes

## Objectiu

L'objectiu d'aquest projecte és desenvolupar una aplicació de gestió de contactes que permeti a l'usuari afegir, eliminar i visualitzar contactes de manera senzilla i eficient. A més, el programa ha de validar les dades introduïdes per assegurar que la informació sigui correcta i coherent.

## Funcionalitats a implementar

### Afegir un contacte

- Se li demana a l'usuari que indiqui el nom del contacte, el número de telèfon i l'adreça de correu electrònic.
- El programa ha de validar que el número de telèfon sigui vàlid (un número de 9 dígits sense espais ni caràcters especials).
- També ha de verificar que l'adreça de correu electrònic tingui un format correcte (per exemple, ha de contenir `@` i un domini).
- No es pot guardar el contacte si aquest ja existeix a la llista (nom, telèfon o correu duplicat).

### Eliminar un contacte

- Se li demana a l'usuari que indiqui el nom del contacte que vol eliminar.
- Si el contacte no està a la llista el programa ho ha de notificar

### Mostrar la llista de contactes

- El programa ha de mostrar tots els contactes actuals amb el seu nom, número de telèfon i adreça de correu electrònic en un format agradable per l'usuari.

### Buscar un contacte a partir del número de telèfon

- Se li demanarà que indiqui el número de telèfon del contacte que vol cercar.
- El programa ha de verificar si el número de telèfon està present a la llista de contactes.
- Si el contacte és trobat, s'ha de mostrar la informació completa del contacte, incloent el nom i l'adreça de correu electrònic.
- Si el contacte no es troba, el programa ha de mostrar el missatge: **"Aquest contacte no està a la llista."**

### Sortir del programa

L'usuari ha de poder sortir del programa. Aquest mostrarà un missatge de comiat i finalitzarà l'execució.

### Gestió d'error

- Si l'usuari vol fer una funcionalitat no existent, el programa ha de mostrar un missatge d'error.

### Llista inicial de contactes

Llista inicial de contactes:
- Joan, 612345678, joan@example.com
- Maria, 698765432, maria@example.com
- Pere, 678123456, pere@example.com
```python
llista_contactes = [
    {"nom": "Joan", "telèfon": "612345678", "email": "joan@example.com"},
    {"nom": "Maria", "telèfon": "698765432", "email": "maria@example.com"},
    {"nom": "Pere", "telèfon": "678123456", "email": "pere@example.com"}
]
```

## A tenir en compte

- El programa ha de ser amigable i proporcionar retroalimentació clara a l'usuari.
- Us pot ser útil l'ús de [diccionaris](https://www.w3schools.com/python/python_dictionaries.asp).

## Enllaços d'interès

- [Documentació](./Documentació.md) del projecte
- [Avaluació](./Avaluació.md) del projecte

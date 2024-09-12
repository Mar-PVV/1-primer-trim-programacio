# PRÀCTICA 1 - Comandes bàsiques del terminal

En aquesta primera pràctica veurem comandes bàsiques del terminal  Windows CMD (Command Prompt).

## Teoria

### Estructura de les comandes

Les comandes del terminal tenen la següent estructura:

> `nom_comanda <opcions>`

Dit això, comencem. Primer de tot obrim el terminal.

### `dir` Command

The dir (**dir**ectory) command lists directory contents, including files and subdirectories. The syntax for the command is:

```bash
dir <drive><path><filename> <options>
```

Primer de tot provem només amb `dir`:

```bash
dir 
```

Ara, prova de mirar el contingut d'una de les carpetes de la teva ubicació actual.

### `cd` Command

The cd (**c**hange **d**irectory) command shows or changes the current location. The syntax for the command is:

```bash
cd <directory>
```

The directory parameter is optional, and without it, the command prints the current working directory.

To change to the parent directory, use the following shortcut:

```bash
cd ..
```

Truc!
> Amb un clic al `Tab` et sortiran les carpetes on pots anar. Clicant successivament `Tab` se't escriurà directament el nom de la carpeta a la línia de comandes.
>
> També pots clicar `Tab` un cop començat el nom de la carpeta i llavors se't completarà automàticament.

A tenir en compte!
> Cal destacar que amb l'ús de la línia de comandes és difícil interectuar amb carpetes i fitxers que tenen espais o accents en el seu nom.

### `md` Command

The md or mkdir (**m**ake **d**irectory) commands create a new directory or subdirectory. The command syntax is:

```bash
md <path>
```

For example, to make a new subdirectory called Hello in the current location, run:

```bash
md Hello
```

To make a new subdirectory called Hello inside Desktop directory, run:

```bash
md Desktop/Hello
```

> Ull amb la creació de carpetes si aquestes no existeixen o el `path` és erroni.

### `rd` Command

The rd or rmdir commands remove an **empty** directory from the system. The syntax for the commands is:

```bash
rd <path>
```

Attempting to delete a directory with files results in an error message. Add the /s parameter to delete a directory with subdirectories and files to avoid the error message:

```bash
rd /s <path>
```

The command deletes the complete subdirectory tree and all files.

### `echo` Command

The echo command prints a message to the console and controls the settings for the command. The syntax for the command is:

```bash
echo <message>
```

Without any parameters, the command shows the current settings.

To use the command and show a "Hello, world!" message to the screen, run:

```bash
echo "Hello, world!"
```

Amb la comanda `echo` i l'ús de `>` podem guardar el text creat en un fitxer:

```bash
echo "Hello, world!" > hello_word.txt
```

### `type` Command

The type command is a built-in command for showing file contents. The command allows viewing a file directly in CMD without modifying the text.

The syntax for the type command is:

```bash
type <file path>
```

For example, to show the contents of the file called sample_file.txt, run:

```bash
type sample_file.txt
```

The output prints the file's contents to the command line. Use this command to preview files directly in the command prompt.

### `copy` Command

The copy command copies one or multiple files from one location to another. The command syntax is:

```bash
copy <options> <source> <destination>
```

For example, to copy a file's contents into a new file in the same location, use:

```bash
copy sample_file.txt sample_file_copy.txt
```

The command creates the new file and copies all the contents from the source file.

### `del` Command

The del and erase commands delete one or more files. The syntax for the commands is:

```bash
del <options> <file(s)>
erase <options> <files(s)>
```

Both commands permanently delete the specified file or files from a disk and are irretrievable.

For example, to delete a file with the name sample.txt, run:

```bash
del sample.txt
```

### Key Commands & Navigation

Few keyboard commands that are very helpful:

- `Up Arrow`: Will show your last command
- `Down Arrow`: Will show your next command
- `Tab`: Will auto-complete your command
- `Ctrl + L`: Will clear the screen
- `Ctrl + C`: Will cancel a command
- `Ctrl + R`: Will search for a command
- `Ctrl + D`: Will exit the terminal

## Pràctica

1. Crea la carpeta de `Test` en l'escriptori del teu ordinador.
2. Dins de la carpeta Test crea `learning.txt` que contingui el següent text: `Hola! Estic aprenent a utilitzar la consola!`.
3. Ves a l'escriptori i crea una nova carpeta anomemanda `Test2` i dins d'aquesta una altra anomanada `Test2-filla`.
4. Ves fins a la carpeta `Test2-filla`.
5. Des d'aquí copia el fitxer `learning.txt` a la carpeta `Test2-filla`.
6. Mostra el resultat a la professora.
7. Suprimeix totes les carpetes i documents creats.
8. Crea la carpeta on anirà tot el material de l'optativa de Programació. Com a recomanació, no utilitzis espais i crea-la en un lloc fàcilment accessible des del terminal, per exemple en l'escriptori.

## Webs interessants

[Més comandes de Windows](https://phoenixnap.com/kb/cmd-commands#ftoc-heading-70)

[Comandes de Linux/Mac](https://gist.github.com/bradtraversy/cc180de0edee05075a6139e42d5f28ce)

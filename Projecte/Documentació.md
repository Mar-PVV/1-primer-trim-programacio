# Documentació del projecte

## Comentaris en el codi

Per assegurar que el fitxer Python del projecte de la llista de la compra sigui clar i accessible, és fonamental incloure comentaris adequats que expliquin el funcionament del codi. A continuació, es detallen algunes directrius per assegurar que el codi sigui accessible i fàcil d'entendre per a altres desenvolupadors o per a vosaltres mateixos en el futur.

1. **Comentaris Generals:**
   - Inclou un comentari al principi del fitxer que descrigui breument l'objectiu del programa i les funcionalitats que implementa.

   ```python
   # Programa de gestió de la llista de la compra.
   # Permet afegir, eliminar i mostrar articles de la llista de la compra.
   # També gestiona missatges d'error si es produeixen accions no vàlides.
   ```

2. **Comentaris per Funcions:**
   - Si el programa utilitza funcions, afegeix un comentari a l'inici de cada funció per explicar el seu propòsit, els arguments d'entrada i el valor de retorn.

   ```python
   def afegir_element(llista, element):
       """
       Afegeix un element a la llista de la compra.
       Si l'element ja existeix, no s'afegeix i es mostra un missatge.
       :param llista: La llista actual de la compra.
       :param element: L'element que es vol afegir.
       :return: None
       """
   ```

3. **Comentaris en Blocs de Codi:**
   - Utilitza comentaris per explicar blocs de codi que poden ser difícils de seguir. Aquests comentaris poden ajudar a aclarir la lògica que s'està implementant.

   ```python
   # Comprovar si l'element ja està a la llista
   if element in llista:
       print("Aquest element ja està a la llista.")
   else:
       llista.append(element)
       print("Element afegit a la llista.")
   ```

## Fitxer Markdown

A més dels comentaris al codi, és essencial proporcionar una documentació clara i estructurada en un fitxer Markdown (README.md). Aquesta documentació ha d'incloure els següents apartats:

1. **Descripció del Projecte:**
   - Explicació general del projecte, el seu objectiu i les funcionalitats principals.

   ```markdown
   # Gestor de la Llista de la Compra
   Aquest programa permet gestionar una llista de la compra, afegint i eliminant articles, així com mostrant la llista actual.
   ```

2. **Interacció amb l'usuari:**
   - Instruccions sobre com l'usuari ha de interactuar amb el programa.

   ```markdown
   ## Interacció amb l'usuari
   En executar el programa, aquest mostra a l'usuari les següents opcions. L'usuari ha d'introduir...
   ```

3. **Exemples d'Ús:**
   - Proporcionar exemples d'entrades i les sortides esperades per ajudar els usuaris a entendre com utilitzar el programa correctament.

   ```markdown
   ## Exemples d'Ús
   - Afegir "maduixes": Element afegit a la llista.
      ```bash
         Què vols fer? 2
         Quin producte vols afegir a la llista? Maduixes
         Maduixes afegides a la llista de la compra!
         Què vols fer ara?
      ```
   - Eliminar "tomàquets": Element eliminat de la llista.
   - Mostrar llista: ['suc de taronja', 'maduixes', ...]
   ```

4. **Funcionament del Programa:**
   - Descripció de com funciona el programa, explicant per blocs el codi.

    ```markdown
    ## Funcionament
    1. En executar el programa, el programa mostra a l'usuari les diferents funcionalitats d'aquest.
       ```python
         <bloc de codi que mostra les opcions a l'usuari.>
       ```
    2. Afegir element
       ```python
         <bloc de codi/funció que afegeix un element a la llista.>
       ```

    ```

5. **Autors:**
   - Mencionar els membres de l'equip que han treballat en el projecte.

   ```markdown
   ## Autors
   - Nom de l'autor 1
   - Nom de l'autor 2
   ```

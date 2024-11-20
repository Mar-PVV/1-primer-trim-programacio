def calcul_nota(llista_notes, llista_percentatges):
    if len(llista_notes) != len(llista_percentatges):
        print("Error, falten notes o percentatges per introduir.")
        return None
    
    for nota in llista_notes:
        if type(nota) is not float or nota > 10 or nota < 0:
            print("Error, hi ha alguna nota incorrecta.")
            return None
    
    for percentatge in llista_percentatges:
        if type(percentatge) is not int or percentatge > 100 or percentatge < 0 or sum(llista_percentatges) != 100:
            print("Error, hi ha algun percentatge incorrecte.")
            return None

    nota_final = 0 
    num_notes = len(llista_notes)

    for i in range(num_notes):
        nota_final += llista_notes[i] * llista_percentatges[i] / 100

    return nota_final
    
notes = [5.2, 4.9, 'aasdf']
percentatges = [10, 20, 70]
print(calcul_nota(notes, percentatges))
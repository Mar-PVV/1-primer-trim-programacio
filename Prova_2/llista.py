llista_compra = [
    "pomes", "ous", "llet", "pa", "patates", "formatge", "maduixes", "tomàquets",    
    "cereals", "xocolata", "maduixes", "iogurt", "ous", "suc de taronja", "cogombres", 
    "pomes", "pasta", "maduixes", "espinacs", "ous", "alvocat", "nous", "mel", "plàtans", 
    "maduixes", "bròquil", "ous", "llenties", "cebes", "pebrot vermell", "ous", 
    "pastanagues", "taronja", "arròs", "peix", "formatge", "pomes"]

print(llista_compra)

llista_compra.sort()

print('Llista de la compra ordenada:')
print(llista_compra)

repetits = []
num_repeticions = []

for item in llista_compra:
    num_item = llista_compra.count(item)
    if num_item > 1:
        if item not in repetits:
            repetits.append(item)
            num_repeticions.append(num_item)

print('Elements repetits:')
for i in range(len(repetits)):
    print(repetits[i] + ' - ' + str(num_repeticions[i]))

opcio = int(input('Clica 1 si vols deixar la llista igual. Clica 2 si vols borrar els elements repetits: '))

if opcio == 1:
    print(llista_compra)

elif opcio == 2:
    for item in repetits:
        repeticions_item = num_repeticions[repetits.index(item)]
        for i in range(1, repeticions_item):
            llista_compra.remove(item)
    print(llista_compra)
    
else:
    print('Opció incorrecta')
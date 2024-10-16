import random

mes = random.randint(1,12)

if mes == 2:
    print(El febrer té 28 dies.)
elif mes == 4 and mes == 6 and mes == 9 and mes == 11:
    print(El mes seleccionat( + str(mes) + ) té 30 dies.)
else mes == 1 and mes == 3 and mes == 5 and mes == 7 and mes == 8 and mes == 10 and mes == 12:
    print(El mes seleccionat( + str(mes) + ) té str(31) dies.)
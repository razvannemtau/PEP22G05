
lst = []
while True:

    numar = input("Introduceti un numar (cand v-ati saturat,apasati q): ")
    if numar == 'q':
        break
    try:
        numar = int(numar)
    except ValueError:
        print('valoare introdusa este incorecta')
    else:
        lst.append(numar)
# Suma numarului de pe pozitia 1 si 2.
print("O sa adaugam numarul 2 si 3.")
try:
    print("lst[1] + lst[2] = ", lst[1] + lst[2])
except IndexError:
    print("Prea putine numere")
else:
    # Divizia primelor 2 numere din lista
    print("Divizia primelor 2 numere din lista este: ")
    try:
        print("lst[0] / lst[1] = ", lst[0] / lst[1])
    except ZeroDivisionError:
        print('Nu se poate imparti la Zero')
    print('Prea putine valori')
    # Suma tuturor numerelor din lista
    sum = 0
    for i in lst:
        sum += i
    print("Suma tuturor numerelor din lista este: ", sum)
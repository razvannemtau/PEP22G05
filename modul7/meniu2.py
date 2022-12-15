from app4 import Haine
from app4 import Accesorii

produse = []
h1 = Haine("Pantaloni", 100, 3)
a1 = Accesorii("Bratara", 100, "argint", 4)
produse.append(h1)
produse.append(a1)


def vizualizare(produse):
    for produs in produse:
        print(produs)


def meniu():
    meniu = {"1": "Adaugare produs", "2": vizualizare, "3": quit}
    while True:
        optiune = input("Optiuni:\n1.Adaugare produs\n2.Vizualizati\n3.Iesire\n").strip()
        try:
            meniu[optiune](produse)
        except KeyError:
            print("Incorrect value! try again... ")


meniu()

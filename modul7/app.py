class Haine:
    nume = ""
    pret = 0
    stoc = 0
    def __init__(self, nume, pret, stoc):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc

    def __str__(self):
        f = f"\n -------------- " \
            f"\n{self.__class__.__name__} " \
            f"\n -------------- " \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}"
        return f
class Accesorii:

    def __init__(self, nume, pret, material, stoc):
        self.nume = nume
        self.pret = pret
        self.material = material
        self.stoc = stoc

    def __str__(self):
        f = f"\n -------------- " \
            f"\n{self.__class__.__name__} " \
            f"\n -------------- " \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}" \
            f"\n Material = {self.material}"
        return f


if __name__ == '__main__':
    bratara = Accesorii ('bratara', 100,'aur', 50,)
    bluze = Haine("bluze", 10, 5)
    print(bluze.pret)
    print(bratara.material)
    print(bluze)
    print(bratara)




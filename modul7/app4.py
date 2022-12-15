class Haine:
    nume = ""
    pret = 0
    stoc = 0
    def __init__(self, nume, pret, stoc, **kwargs):
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
class Accesorii(Haine):

    def __init__(self, nume, pret, material, stoc, **kwargs):
        super().__init__(nume, pret, stoc, **kwargs)
        self.material = material


    def __str__(self):
        f = super().__str__()
        f += f"\n Material = {self.material}"
        return f

class Incaltaminte(Haine):

    def __int__(self, nume, pret, stoc, **kwargs):
        super(Incaltaminte, self).__init__(nume, pret, stoc)
        for key, value in kwargs.item():
            setattr(self, key, value)

    def __str__(self):
        f = super().__str__()
            f"\n Material = {self.material}" \
            f"\n {20 * '-'}
        return f


if __name__ == '__main__':
    bratara = Accesorii ('bratara', 100,'aur', 50,)
    bluze = Haine("bluze", 10, 5)
    print(bluze.pret)
    print(bratara.material)
    print(bluze)
    print(bratara)
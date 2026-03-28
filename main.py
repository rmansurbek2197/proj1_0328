class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

t1 = Talaba("Ali", 20)
print(t1.ism, t1.yosh)


class Avto:
    def __init__(self, model, tezlik=0):
        self.model = model
        self.tezlik = tezlik

    def tezlash(self, qiymat):
        self.tezlik += qiymat

a = Avto("BMW")
a.tezlash(50)
print(a.tezlik)


class Kitob:
    def __init__(self, nom, muallif):
        self.nom = nom
        self.muallif = muallif

    def info(self):
        return f"{self.nom} - {self.muallif}"

k = Kitob("Python", "Guido")
print(k.info())

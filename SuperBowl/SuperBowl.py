print("3. feladat")

# Ssz;Dátum;Győztes;Eredmény;Vesztes;Helyszín;VárosÁllam;Nézőszám

class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(';')

        self.ssz = reszletek[0]
        self.date = reszletek[1]
        self.winner = reszletek[2]
        self.eredmeny = reszletek[3]
        self.vesztes = reszletek[4]
        self.helyszin = reszletek[5]
        self.varosallam = reszletek[6]
        self.nezoszam = int(reszletek[7])

    def __str__(self):
        return f"{self.date}, {self.helyszin}: {self.winner} - {self.vesztes} ({self.eredmeny})"
    

print("\nSuper Bowl döntői")

fin = open("SuperBowl.txt", "rt", encoding="utf8")
adatsorok = fin.read().split('\n')
fin.close()

dontok = []
for i in range(1, len(adatsorok)):
    if adatsorok[i] != "":
        donto = Donto(adatsorok[i])
        dontok.append(donto)


for it in dontok:
    print(it)
import random

#0
print("Tanuló adatai ömlesztve.")

#1
adatSorBe=input("Kérem a tanuló adatait ';'-el elválasztva: ")
reszletek = adatSorBe.split(';')

tanulo={}
tanulo["nev"]=reszletek[0]
tanulo["szid"]=reszletek[1]
tanulo["magassag"]=int(reszletek[2])
tanulo["tomeg"]=float(reszletek[3].replace(',' , '.'))


#2
tanulo["nev"]="Váradi László"
tanulo["szid"]=str(random.randint(2000, 2010)) + '.' + str(random.randint(1,12)) + '.' + str(random.randint(1,28))
tanulo["magassag"]=random.randint(150, 220)
tanulo["tomeg"]=random.randint(50, 110) + random.random()

#3
reszletek[0]=tanulo["nev"]
reszletek[1]=tanulo["szid"]
reszletek[2]=str(tanulo["magassag"])
reszletek[3]=str(tanulo["tomeg"])
adatSorKi = "#".join(reszletek)
print(adatSorKi)
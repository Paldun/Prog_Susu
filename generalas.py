import random

#0
print("Osztályzatok generálása.")

#1
db = int(input("Kérem az osztályzatok számát: "))

osztalyzatok = []
#mivel ismerjük a darabok számát - ezért a generálást előre meghatározott lépésszámú ciklusban végezzük
for i in range(db):
    oszt = random.randint(1,5)
    osztalyzatok.append(oszt)

#2-3
print(osztalyzatok)
import math

#függvények
def HaromszogKerulete(aa, bb, cc):
    return aa + bb + cc

def HaromszogTerulete(aa, bb, cc):
    s = HaromszogKerulete(aa, bb, cc) / 2
    TT = math.sqrt( s*(s-aa)*(s-bb)*(s-cc) )
    return TT

def Szog(m1, m2, sz):    #
    ertek=(m1**2 + m2**2 - sz**2)/(2*m1*m2)
    return math.degrees( math.acos(ertek) )

#0
print("Háromszög feldolgozása függvények segítségével.")

#1
temp=input("Kérem az oldalakat ';'-el elválasztva: ")
reszletek = temp.split(';')
a = float(reszletek[0].replace(',' , '.'))
b = float(reszletek[1].replace(',' , '.'))
c = float(reszletek[2].replace(',' , '.'))

#2
K = HaromszogKerulete(a, b, c)
T = HaromszogTerulete(a, b, c)
alfa = Szog(b, c, a)
betta = Szog(a, c, b)
gamma = Szog(a, b, c)


#3
print(f"A(z) {a:.2f}cm, {b:.2f}cm és {c:.2f}cm oldalhosszúságú háromszög kerülete: {K:.2f}cm")
print(f"A(z) {a:.2f}cm, {b:.2f}cm és {c:.2f}cm oldalhosszúságú háromszög területe: {T:.2f}cm^2")
print(f"alfa: {alfa:.2f}°")
print(f"betta: {betta:.2f}°")
print(f"gamma: {gamma:.2f}°")
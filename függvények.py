#functions
def fuggveny(xx):
    return 3*xx**2 - 5*xx + 6

#0
print("Függvény táblázatban")

#1
a = float(input("a = ").replace(',' , '.'))
b = float(input("b = ").replace(',' , '.'))
d = float(input("d = ").replace(',' , '.'))

#2
if a>b:
    a, b = b, a

x = []
y = []
while a <= b:
    x.append(a)
    y.append(fuggveny(a))
    a += d

#3
print(f"{'x':^11s} | {'y':^11s}")
print("-"*25)
for i in range(len(x)):
    print(f"{x[i]:11.2f} | {y[i]:11.2f}")
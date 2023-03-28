#functions
def fibonacci(nn):
    if nn == 0:
        return 0
    elif nn == 1:
        return 1
    else:
        return fibonacci(nn-1) + fibonacci(nn-2)

#0
print("Fibonacci sorozat elemei")

#1
a = float(input("a = ").replace(',' , '.'))
b = float(input("b = ").replace(',' , '.'))

#2
if a>b:
    a, b = b, a

fibJo = []
n=0
while True:
    elem = fibonacci(n)
    if elem >= a and elem <= b:
        fibJo.append(elem)
    elif elem>b:
        break
    n+=1

#3
tempStr = []
for item in fibJo:
    tempStr.append( str(item) )

kiiras = "; ".join(tempStr)
print(kiiras)
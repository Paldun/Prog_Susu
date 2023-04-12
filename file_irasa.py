import math

def szogFok(sz, m1, m2):
    return math.degrees(math.acos((m1**2 + m2**2 - sz**2)/(2*m1*m2)))

fbe = open('fileok_edit/haromszogek.txt', 'rt', encoding='utf-8')
fki = open('fileok_edit/szogek.txt', 'wt', encoding='utf-8')
szoveg = fbe.read()
sorok = szoveg.split("\n")

szogekLines = []
for item in sorok:
    if item != '':
        reszletek = item.split(';')
        a = float(reszletek[0].replace(',','.'))    
        b = float(reszletek[1].replace(',','.'))    
        c = float(reszletek[2].replace(',','.'))    

        alfa = szogFok(a,b,c)
        beta = szogFok(b,a,c)
        gamma = szogFok(c,a,b)

        # szogekSzovegesen = (str(alfa), str(beta), str(gamma))
        # szogekSor = ';'.join(szogekSzovegesen)
        szogekSor = f"{alfa:.2f};{beta:.2f};{gamma:.2f}\n"
        szogekLines.append(szogekSor)

# tartalom = '\n'.join(szogekLines)
# fki.writelines(tartalom)

fki.writelines(szogekLines)



fbe.close()
fki.close()
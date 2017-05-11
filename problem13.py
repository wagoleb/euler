name = 'problem15-number.txt'
file = open(name,'r')

suma = []

for line in file:
    suma.append(int(line))



wynik = sum(suma)

wynik2 = str(wynik)

print(wynik2[:10])
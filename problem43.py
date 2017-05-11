listOfPandigital = []


import itertools

lista = itertools.permutations('0123456789')
for item in lista:
    listOfPandigital.append(''.join(item))

print(len(listOfPandigital))
"""************"""



def find(n):
    dividers = [2, 3, 5, 7, 11, 13, 17]
    warunki = []
    for i in range(1, len(n)-2):
        warunki.append(int(n[i:i+3]) % dividers[i - 1] == 0)
        # print("%s : %s" % (int(n[i:i+3]),dividers[i - 1]))
    # print(warunki)
    if all(warunki):
        return True
    else:
        return False
suma = 0
for number in listOfPandigital:
    if find(number):
        suma+=int(number)

print(suma)
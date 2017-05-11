def silnia(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n*silnia(n-1)

suma = 0
for item in str(silnia(100)):
    suma += int(item)

print(suma)
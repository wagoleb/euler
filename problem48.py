end = 1000
lista = [x**x for x in range(1,end+1)]
value = str(sum(lista))

print(value[-10:])

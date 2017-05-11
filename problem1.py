suma = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        suma += i
print(suma)

# def podzielna(x):
#     if x % 3 == 0 or x % 5 ==0:
#         return x
#     else:
#         return False
#
# lista = filter(podzielna, [x for x in range(1,1000)])
# print(sum(lista))
#
# lista = map(podzielna, [x for x in range(1,1000)])
# print(sum(lista))

from functools import reduce
res = reduce(lambda x,y:x+y,[x for x in range(1,1000) if x % 3 == 0 or x % 5 ==0])
print(res)
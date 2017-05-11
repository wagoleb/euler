def pentagonal(n):
    if n == 1:
        return 1
    else:
        return int((n*((3*n)-1))/2)

def triangle(n):
    if n == 1:
        return 1
    else:
        return int((n*(n+1))/2)

def hexagonal(n):
    if n == 1:
        return 1
    else:
        return int(n*((2*n)-1))

value = 500000

A = set(map(pentagonal, [x for x in range(value)]))
B = set(map(triangle, [x for x in range(value)]))
C = set(map(hexagonal, [x for x in range(value)]))

print(A.intersection(B,C))

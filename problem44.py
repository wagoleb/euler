def pentagonal(n):
    if n == 1:
        return 1
    else:
        return int((n*((3*n)-1))/2)

for i in range(1,11):
    print(pentagonal(i))

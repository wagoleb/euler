def return_itterative_sequence(n):
    if n > 1:
        if n % 2 == 0:
            return int(n / 2)
        else:
            return 3*n+1
    else:
        return 1

en = 13
number = 0
current = 0

for i in range(1,1000000):
    print(i)
    long = 1
    n = i
    while n != 1:
        n = return_itterative_sequence(n)
        long += 1

    if long > current:
        number = i
        current = long

print(number)
print(long)
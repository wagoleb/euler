value = 20
loop = True

def divide(n):
    return [n % x == 0 for x in range(1,21)]

while loop:
    print(value)
    if all(divide(value)):
        print(value)
        loop = False
    else:
        value += 20
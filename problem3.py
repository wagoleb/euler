#problem4.py
from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.


def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))


value = 600851475143

for i in range(1,int(value/2)):
    if is_prime(i):
        # print(i)
        if value % i == 0:
            print("XXXX",i)

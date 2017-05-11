#problem10
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


value = 2000000
allprimes = []
for i in range(1,value+1):
    if is_prime(i):
        allprimes.append(i)

print(sum(allprimes))

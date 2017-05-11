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


max_prime = 0
length = 0
for i in range(1000000,1,-1):
    primes = []
    for value in range(1,i):
        if is_prime(value):
            primes.append(value)
    if primes and is_prime(sum(primes)):
        # print(sum(primes)," = ",primes)
        if len(primes) > length:
            max_prime = value
            length = len(primes)

print("value: ",max_prime, " length: ", length)
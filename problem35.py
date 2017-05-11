def is_prime(n):
    if n <= 2:
        if n == 2:
            return True
        elif n == 1:
            return True
    elif n > 2:
        for i in range(3, int(n / 2)):
            if n % i == 0:
                return False
    else:
        return True




for i in range(1,1000):
    if is_prime(i):
        print("%s, " % i)
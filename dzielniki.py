def return_factors(n,factor=2):
    list = []
    if n > 1 and n % factor == 0:
        list.append(factor)
        return return_factors(int(n/2))
    elif n > 1 and n % factor != 0:
        return return_factors(int(n/2),factor+1)
    elif n == 1:
        return list

print(return_factors(24))

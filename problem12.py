def triangle_numbers(n):
    if n == 1:
        return 1
    else:
        return n+triangle_numbers(n-1)

def return_dividers(n):
    list = []
    for i in range(1,n+1):
        if n % i == 0:
            list.append(i)
    return list

i = 1
while True:
    number = triangle_numbers(i)
    divs = return_dividers(number)
    if len(divs) >= 500:
        print(number)
        print(divs)
        break

    i+=1
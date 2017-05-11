def silnia(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n*silnia(n-1)

for i in range(3,200):
    nr_to_str = str(i)
    tab = []
    for item in nr_to_str:
        tab.append(silnia(int(item)))
    if sum(tab) == i:
        print(i)
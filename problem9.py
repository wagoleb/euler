for a in range(1,1001):
    for b in range(a,1001):
        for c in range(b,1001):
            if all([sum([a, b, c]) == 1000, (a ** 2) + (b ** 2) == (c ** 2)]):
                print("a=%s, b=%s,c=%s, product=%s" % (a,b,c,a*b*c))
                break


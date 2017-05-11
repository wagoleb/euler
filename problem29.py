a = 2
b = 100
table = []
for x in range(a,b+1):
    for y in range(a,b+1):
        if x**y not in table:
            table.append(x**y)
table.sort()
print(len(table))

suma = 0
for i in range(2,10000000):
    if i == sum([int(x)**5 for x in str(i)]):
        print(i)
        suma+=i

print("suma: ",suma)
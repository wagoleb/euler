fib = [1,1]
n=1
while len(str(fib[-1])) < 1000:
    fib.append(fib[-2]+fib[-1])
    n+=1

print(fib)
print(int(fib.index(fib[-1]))+1)

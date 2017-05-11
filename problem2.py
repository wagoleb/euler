
def gen_fib(i):
    if i < 3:
        return i
    else:
        return sum([gen_fib(i-2), gen_fib(i-1)])
step = 1
suma = 0
value = 1
while value < 4000000:
    value = gen_fib(step)
    if value % 2 == 0:
        suma += value
    step += 1

print(suma)
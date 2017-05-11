def return_Fib(n):
    if n < 3:
        return 1
    else:
        return return_Fib(n-1)+return_Fib(n-2)
step = 1
while True:
    length = len(str(return_Fib(step)))
    print(length)
    if length == 10:
        print(step)
        break
    else:
        step+=1
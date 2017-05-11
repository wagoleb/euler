def is_a_palindromic(n):
    if str(n) == str(n)[::-1] and len(str(n)) > 1:
        return True
    else:
        return False
value = 0
for a in range(0,1000):
    for b in range(0,1000):
        if is_a_palindromic(a*b):
            if a*b > value:
                value = a*b

print(value)
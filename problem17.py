import inflect

def return_wrod(n):
    p = inflect.engine()
    return p.number_to_words(n)


length = 0

for number in range(1,1001):
    for char in return_wrod(number):
        if char.isalpha():
            length+=1
print(length)
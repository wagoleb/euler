

traingles_numbers = [1,3]

for n in range(1,100):
    if n > 2:
        traingles_numbers.append(int((0.5*n)*(n+1)))



file_name = "p042_words.txt"

f = open(file_name, 'r')

ileJest = 0
wordsList = f.readline().rstrip().replace('"','').split(',')
# print(wordsList)
for word in wordsList:
    suma = 0
    for letter in word:
        suma += ord(letter)-64
    # print("%s = %s" % (word,suma))
    if suma in traingles_numbers:
        ileJest += 1

print("total:", ileJest)



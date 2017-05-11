def returnListOfDividers(n):
    listOfDividers = []
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            listOfDividers.append(i)
    return listOfDividers

# i = 8128
# di = sum(returnListOfDividers(i))
# print(i, di)
#
# j = di
# dj = sum(returnListOfDividers(j))
# print(j, dj)

listOfAmicable = []
for value in range(1,10001):
    di= sum(returnListOfDividers(value))
    if all([value==sum(returnListOfDividers(sum(returnListOfDividers(value)))), value != sum(returnListOfDividers(value))]):
        print(value)
        listOfAmicable.append(value)

print("suma: %s" % sum(listOfAmicable))
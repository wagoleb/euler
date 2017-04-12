file = open("p022_names.txt")
line = file.readline()
file.close()
cleared = [x.replace('"','') for x in line.split(",")]
cleared.sort()

total = 0
for name in cleared:
    alphabetical_value = 0
    for letter in name:
        alphabetical_value+=int(ord(letter)-64)
    position = int(cleared.index(name))+1

    print("{} = letter value: {}, position: {}, product = {}".format(name,alphabetical_value,position,alphabetical_value*position))
    total+=alphabetical_value*position
print(total)


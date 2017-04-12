file_name = "problem18.txt"

f = open(file_name, 'r')

read_table = []
for line in f:
    read_table.append(line.rstrip().split(' '))

new_table = []

for item in read_table:
    new_table.append([int(x) for x in item])

print(new_table)

sums = []
for item in new_table:
    if new_table.index(item) >= 1:
        maxx = len(item)
        for number in item:
            index = int(item.index(number))
            prev_index = int(new_table.index(item))-1
            if index == 0:
                # print("{}+{}".format(number,new_table[prev_index][index]))
                sums.append(number + new_table[prev_index][index])
            # elif index > 0 and index < maxx:


print(sums)
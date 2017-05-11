file_name = "problem18-numbers.txt"
f = open(file_name, 'r')

lines = {}
line_nr = 0
for line in f:
    remove_line = line.rstrip()
    line_stripped = remove_line.split(' ')
    lines.update({line_nr: line_stripped})
    line_nr+=1


f.close()
list_of_max = []
prev_key = 0

for key in lines.keys():
    if len(lines[key]) < 2:
        max_from_line = max(lines[key])
        list_of_max.append(int(max_from_line))
        prev_key = lines[key].index(max_from_line)
    else:
        max_from_line = max([lines[key][prev_key],lines[key][prev_key+1]])
        prev_key = lines[key].index(max_from_line)
        list_of_max.append(int(max_from_line))


print(list_of_max)
print(sum(list_of_max))




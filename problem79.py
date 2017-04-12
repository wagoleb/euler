file_name = "p079_keylog.txt"

f = open(file_name, 'r')
first,second,third = [],[],[]
for line in f:
    first.append(line.rstrip()[0])
    second.append(line.rstrip()[1])
    third.append(line.rstrip()[2])

f.close()

print(first)
print(second)
print(third)

first_set = set(first)
second_set = set(second)
third_set = set(third)

print(first_set)
print(second_set)
print(third_set)
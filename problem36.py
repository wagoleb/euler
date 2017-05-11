def dec_to_bin(x):
    return int(bin(x)[2:])



count = 1
values = []

while True:
    if count > 1000000:
        break
    if all([str(count) == str(count)[::-1],str(dec_to_bin(count)) == str(dec_to_bin(count))[::-1]]):
        values.append(count)
    count +=1

print(sum(values))
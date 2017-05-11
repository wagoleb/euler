for i in range(5,20000000,5):
    if i % 5 == 0:
        nr_to_str = str(i)
        suma = 0
        for item in nr_to_str:
            suma += int(item)**5
        if i == suma:
            print(i)


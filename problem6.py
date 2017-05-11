import math
value = 100

sum_of_the_squares = sum([x**2 for x in range(1,value+1)])

square_of_the_sum = sum([x for x in range(1,value+1)])**2

print(int(math.fabs(sum_of_the_squares-square_of_the_sum)))


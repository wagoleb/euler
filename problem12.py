

import operator
from functools import reduce
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)

def return_nth_triangle_number(pos):
    return sum([x for x in range(1,pos+1)])

i = 1
while True:
    if NumberOfDivisors(return_nth_triangle_number(i)) >= 500:
        print(return_nth_triangle_number(i), " - ", NumberOfDivisors(return_nth_triangle_number(i)))
        break

    else:
        # print(return_nth_triangle_number(i), " - ", NumberOfDivisors(return_nth_triangle_number(i)))
        i += 1
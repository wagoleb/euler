import itertools
step = 1
for item in itertools.permutations([x for x in range(10)]):
    if step == 1000000:
        print("step %s = %s" % (step, item))
    step+=1

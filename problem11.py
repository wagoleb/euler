from functools import reduce

class value():
    def __init__(self,n,pos):
        self.value = n
        self.pos = pos

    def __str__(self):
        return "pos: {0:-2d} x {1:-2d} value: {2:-2d}".format(self.pos[0],self.pos[1],self.value)

class grid():
    def __init__(self,filename):
        self.items = []

        f=open(filename,'r')
        col = 1
        row = 1
        for line in f:
            values = [int(x) for x in line.rstrip().split(' ')]
            row = 1
            for item in values:
                self.add_item(value(item,[col,row]))
                row+=1
            col+=1

    def add_item(self,item):
        self.items.append(item)

    def return_value(self,*positions):
        for index in positions:
            if index in [x.pos for x in self.items]:
                for item in self.items:
                    if index == item.pos:
                        yield item.value
        else:
            return False

    def __getitem__(self, item):
        return self.items[item]


kontener = grid("20x20grid.txt")

size = 20
maxed = 0
# left
for col in range(1,size+1):
    for row in range(1,size+1):
        if row <= size-3:
            list = [x for x in kontener.return_value([col,row],[col,row+1],[col,row+2],[col,row+3])]
            # print([col,row],[col,row+1],[col,row+2],[col,row+3])
            product = reduce(lambda x, y: x * y, list)
            if product > maxed:
                maxed = product
# right
for col in range(1,size+1):
    for row in range(1,size+1):
        if col <= size-3:
            list = [x for x in kontener.return_value([col,row],[col+1,row],[col+2,row],[col+3,row])]
            # print([col,row],[col+1,row],[col+2,row],[col+3,row])
            product = reduce(lambda x, y: x * y, list)
            if product > maxed:
                maxed = product


# diagonally
for col in range(1,size+1):
    for row in range(1,size+1):
        if col <= size-3 and row <= size-3:
            list = [x for x in kontener.return_value([col,row],[col+1,row+1],[col+2,row+2],[col+3,row+3])]
            # print([col,row],[col+1,row+1],[col+2,row+2],[col+3,row+3])
            product = reduce(lambda x, y: x * y, list)
            if product > maxed:
                maxed = product

# diagonally 2
for col in range(1,size+1):
    for row in range(1,size+1):
        if col <= size-3 and row <= size-3:
            list = [x for x in kontener.return_value([col,row],[col-1,row+1],[col-2,row+2],[col-3,row+3])]
            # print([col,row],[col-1,row+1],[col-2,row+2],[col-3,row+3])
            product = reduce(lambda x, y: x * y, list)
            if product > maxed:
                maxed = product


print(maxed)

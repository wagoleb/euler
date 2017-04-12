
class node():
    def __init__(self,name,parents=[],childs=[]):
        self.name = name
        self.weight = 1
        self.childs, self.parents = [], []
        if parents:
            self.update_parents(*parents)

        if childs:
            self.update_childs(*childs)

    def update_weight(self):
        if not self.parents:
            self.weight = 1
        else:
            self.weight = 0
            for item in self.parents:
                self.weight += item.weight

    def update_childs(self,*args):
        if args:
            for item in args:
                self.childs.append(item)

    def update_parents(self,*args):
        if args:
            for item in args:
                self.parents.append(item)

class nodes_container():
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def __getitem__(self, item):
        return self.items[item]

    def return_size(self):
        return len(self.items)

    def return_id_by_name(self,name):
        for item in self.items:
            if name == item.name:
                return item

kontener = nodes_container()
size = 50
for a in range(1,size+1):
    for b in range(1,size+1):
        kontener.add_item(node([a,b]))


for item in kontener:
    col = item.name[0]
    row = item.name[1]
    if col < size and row < size:
        item.update_childs(kontener.return_id_by_name([col,row+1]),kontener.return_id_by_name([col+1,row]))
    elif col == size and row < size:
        item.update_childs(kontener.return_id_by_name([col, row + 1]))
    elif col < size and row == size:
        item.update_childs(kontener.return_id_by_name([col +1, row]))

for item in kontener:
    col = int(item.name[0])
    row = int(item.name[1])
    if col > 1 and row > 1:
        item.update_parents(kontener.return_id_by_name([col,row-1]),kontener.return_id_by_name([col-1,row]))


for item in kontener:
    item.update_weight()


print(kontener[-1].weight)
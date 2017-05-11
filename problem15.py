class find_ways():

    def __init__(self, size):
        self.size = size
        self.current = [1,1]
        self.right_completed = False

    def go_down(self,point):
        new = [point[0]+1, point[-1]]
        return new

    def go_right(self,point):
        new = [point[0], point[-1]+1]
        return new

    def can_both(self,point):
        if point[0] < self.size and point[-1] < self.size:
            return True
        else:
            return False

    def can_right(self,point):
        if not point[0] < self.size and point[-1] < self.size:
            return True
        else:
            return False

    def can_down(self,point):
        if point[0] < self.size and not point[-1] < self.size:
            return True
        else:
            return False

    def at_the_end(self,point):
        if point[0] == self.size and point[-1] == self.size:
            return True
        else:
            return False

    def search(self):
        if not self.right_completed:
            if self.can_right(self.current):
                self.go_right()
            else:
        else:


size = 21
inst = find_ways(int(size))

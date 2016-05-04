class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist, num):
    line = Queue()
    for i in namelist:
        line.enqueue(i)
    while line.size() > 1:
        for i in range(num):
            line.enqueue(line.dequeue())
        line.dequeue()
    return line.dequeue()



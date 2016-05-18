class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        found = False
        current = self.head
        while not found and current is not None:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found

    def remove(self, item):
        found = False
        current = self.head
        prev = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev is None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())

    def append(self, item):
        end = False
        current = self.head
        while not end:
            if current.getNext() == None:
                end = True
            current = current.getNext()
        current.setNext(Node(item))

    def insert(self, item, index):
        temp = Node(item)
        current = self.head
        prev = None
        for i in range(index):
            prev = current
            current = current.getNext()
        prev.setNext(temp)
        temp.setNext(current)


"""
link = LinkedList()
link.add(10)
link.add(3)
link.add(1345)
link.append(46)
print link.size()
link.remove(3)
print link.size()
"""

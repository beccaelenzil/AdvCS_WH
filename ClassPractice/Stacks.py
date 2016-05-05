class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def parenChecker(parens):
    storage = Stack()
    for i in parens:
        if i == "(":
            storage.push(i)
        elif i == ")":
            if storage.isEmpty():
                return False
            else:
                storage.pop()
    if storage.isEmpty():
        return True
    else:
        return False


def balSymChecker(parens):
    storage = Stack()
    for i in parens:
        if i in "({[":
            storage.push(i)
        elif i in ")}]":
            peek = storage.peek()
            if storage.isEmpty():
                return False
            elif (i == ")" and peek == "(") or (i == "]" and peek == "[") or (i == "}" and peek == "{"):
                storage.pop()
            else:
                return False
    if storage.isEmpty():
        return True
    else:
        return False


def divideBy2(string):
    storage = Stack()
    while string != 0:
        storage.push(int(string) % 2)
        string = int(string) // 2
    return "".join([str(storage.pop()) for j in range(storage.size())])


def divideBy2baseN(string, N):
    storage = Stack()
    test = -1
    increment = 0
    while test > 0:
        test = int(string) - N ^ increment
    actNum = 0
    num = int(string)
    for i in range(0, increment - 1, -1):
        if num - N^i > 0:
            num -= N^i
            actNum += N^i
    while actNum != 0:
        storage.push(actNum % 2)
        actNum = actNum // 2
    return "".join([str(storage.pop()) for j in range(storage.size())])

print divideBy2baseN("10", 16)
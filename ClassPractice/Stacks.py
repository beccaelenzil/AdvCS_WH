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
        if i == "(" or i == "[" or i == "{":
            storage.push(i)
        elif i == ")" or i == "]" or i == "}":
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

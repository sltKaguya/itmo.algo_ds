f_in = open("postfix.in")
f_out = open("postfix.out", "w")

class Stack():

    def __init__(self):
        self.last = None

    def insert(self, value):
        elem = Element(value)
        elem.next = self.last
        self.last = elem

    def remove(self):
        value = self.last.value
        self.last = self.last.next
        return value

class Element():

    def __init__(self, value):
        self.value = value
        self.next = None

command = f_in.readline().strip().split()
stack = Stack()
for i in command:
    if i == "+":
        stack.insert(stack.remove() + stack.remove())
    elif i == "-":
        stack.insert(-1*(stack.remove() - stack.remove()))
    elif i == "*":
        stack.insert(stack.remove() * stack.remove())
    else:
        stack.insert(int(i))

f_out.write(str(stack.remove()))
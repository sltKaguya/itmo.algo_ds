f_in = open("stack.in")
f_out = open("stack.out", "w")

class LinkedList():

    def __init__(self) -> None:
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

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

stack = LinkedList()
ans = []
m = int(f_in.readline().strip())
for i in range(m):
    command = f_in.readline().strip()
    if command == "-":
        ans.append(stack.remove())
    else:
        stack.insert(command.split()[1])

f_out.write("\n".join(ans))
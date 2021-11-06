f_in = open("queue.in")
f_out = open("queue.out", "w")

class Queue():

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def insert(self, value):
        elem = Element(value)
        if self.first:
            self.last.next = elem
            self.last = elem
        else:
            self.first = elem
            self.last = elem

    def remove(self):
        value = self.first.value
        self.first = self.first.next
        return value

class Element():

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

ans = []
queue = Queue()
m = int(f_in.readline().strip())
for i in range(m):
    command = f_in.readline().strip()
    if command == "-":
        ans.append(queue.remove())
    elif len(command) > 1:
        queue.insert(command.split()[1])

f_out.write("\n".join(ans))
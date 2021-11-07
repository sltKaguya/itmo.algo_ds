f_in = open("brackets.in")
f_out = open("brackets.out", "w")

class Stack():

    def __init__(self):
        self.last = None

    def insert(self, value):
        elem = Element(value)
        elem.next = self.last
        self.last = elem

    def remove(self):
        self.last = self.last.next

class Element():

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

ans = []
for line in f_in.readlines():
    line = line.strip()
    stack = Stack()
    check = True
    for i in line:
        if i == "(" or i == "[":
            stack.insert(i)
        elif not stack.last:
            check = False
            break
        elif (stack.last.value == "(" and i == ")"\
                or stack.last.value == "[" and i == "]"):
            stack.remove()
        else:
            check = False
    if check:
        ans.append("YES")
    else:
        ans.append("NO")

f_out.write("\n".join(ans))
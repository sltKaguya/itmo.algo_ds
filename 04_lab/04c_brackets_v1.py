f_in = open("brackets.in")
f_out = open("brackets.out", "w")

class Stack():

    def __init__(self) -> None:
        self.last = None
    
    def insert(self, value):
        elem = Element(value)
        if not self.last:
            self.last = elem
        else:
            if self.last.value == "(" and value == ")"\
                or self.last.value == "[" and value == "]":
                self.last = self.last.next
            else:
                elem.next = self.last
                self.last = elem

    def check(self):
        if self.last:
            return False
        else:
            return True

class Element():

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

ans = []
for line in f_in.readlines():
    line = line.strip()
    stack = Stack()
    for i in line:
        stack.insert(i)

    if stack.check():
        ans.append("YES")
    else:
        ans.append("NO")  

f_out.write("\n".join(ans))  
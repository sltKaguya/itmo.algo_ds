f_in = open("set.in")
f_out = open("set.out", "w")

size = 100000
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList():

    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, value):
        elem = Node(value)
        if not(self.exists(value)):
            if self.first:
                self.last.next = elem
                elem.previous = self.last
                self.last = elem
            else:
                self.first = elem
                self.last = elem
        else:
            pass

    def exists(self, value):
        elem = self.first

        while elem:

            if elem.value == value:
                return elem

            else:
                elem = elem.next

        return None

    def delete(self, value):
        elem = self.exists(value)

        while elem:

            if elem.value == value:

                if elem.previous:
                    elem.previous.next = elem.next

                    if elem.next:
                        elem.next.previous = elem.previous

                else:
                    self.first = elem.next

                    if elem.next:
                        elem.next.previous = None

                return

            elem = elem.next
        return

commands = [i.strip().split() for i in f_in.readlines()]
hash_table = [0]*size
for i in hash_table:
    hash_table[i] = LinkedList()

for command in commands:
    index = int(command[1]) % size
    value = int(command[1])

    if command[0] == "insert":
        hash_table[index].insert(value)

    elif command[0] == "exists":

        if hash_table[index].exists(value):
            print("true", file=f_out)

        else:
            print("false", file=f_out)

    elif command[0] == "delete": 
        hash_table[index].delete(value)

f_out.close()
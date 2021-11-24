f_in = open("set.in")
f_out = open("set.out", "w")

size = 500000
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList():

    def __init__(self):
        self.first = None

    def insert(self, value):
        elem = Node(value)
        if not(self.exists(value)):
            if self.first:
                self.first.previous = elem
            elem.next = self.first
            self.first = elem

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
        if elem:
            if elem.next:
                elem.next.previous = elem.previous
            if elem.previous:
                elem.previous.next = elem.next
            else:
                self.first = elem.next
            
hash_table = [LinkedList() for i in range(size)]

command = f_in.readline().strip().split()
while command:
    value = int(command[1])
    index = value % size

    if command[0] == "insert":
        hash_table[index].insert(value)

    elif command[0] == "exists":
        if hash_table[index].exists(value):
            print("true", file=f_out)
        else:
            print("false", file=f_out)

    elif command[0] == "delete": 
        hash_table[index].delete(value)

    command = f_in.readline().strip().split()

f_out.close()
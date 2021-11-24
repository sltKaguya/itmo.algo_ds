f_in = open("set.in")
f_out = open("set.out", "w")

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
        if self.first:
            self.last.next = elem
            elem.previous = self.last
            self.last = elem
        else:
            self.first = elem
            self.last = elem

    def exists(self, value):
        elem = self.first
        while elem:
            if elem.value == value:
                print("found", elem.value)
                return elem
            else:
                print("go next", elem.value)
                elem = elem.next
        print("didn't found")
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
                        self.first = elem.next
                return
            elem = elem.next
        return

class HashTable():

    def __init__(self):
        self.size = 100000
        self.list = [LinkedList()] * self.size

    def h_insert(self, value):
        index = value % self.size
        if not(self.list[index].exists(value)):
            self.list[index].insert(value)

    def h_exists(self, value):
        index = value % self.size
        if self.list[index].exists:
            return "true"
        else:
            return "false"

    def h_delete(self, value):
        index = value % self.size
        self.list[index].delete(value)

commands = [i.strip().split() for i in f_in.readlines()]
hash_table = HashTable()

for command in commands:
    if command[0] == "insert":
        hash_table.h_insert(int(command[1]))

    elif command[0] == "exists":
        print(hash_table.h_exists(int(command[1])), file=f_out)

    elif command[0] == "delete":
        hash_table.h_delete(int(command[1]))

    else:
        pass

for elem in hash_table.list:
    print(hash_table.list.first.value)
f_out.close()
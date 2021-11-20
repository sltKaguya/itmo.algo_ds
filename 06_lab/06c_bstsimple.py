f_in = open("bstsimple.in")
f_out = open("bstsimple.out", "w")

class Node():

    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

class BinSearchTree():

    def __init__(self):
        self.root = None

    def insert(self, value):
        elem = Node(value)
        if self.root == None:
            self.root = elem
        else:
            root = self.root
            while root:
                if value > root.value:
                    if root.right:
                        root = root.right
                    else:
                        root.right = elem
                        elem.parent = root
                        return
                elif value < root.value:
                    if root.left:
                        root = root.left
                    else:
                        root.left = elem
                        elem.parent = root
                        return

    def search(self, value):
        node = None
        root = self.root
        while root:
            if value == root.value:
                node = root
                return node
            elif value > root.value:
                root = root.right
            else:
                root = root.left
        return node

    def exists(self, value):
        if tree.search(value):
            return "true"
        else:
            return "false"

    def next(self, value):
        answer = None
        root = self.root
        while root:
            if value < root.value:
                answer = root
                root = root.left
            else:
                root = root.right
        return answer

    def prev(self, value):
        answer = None
        root = self.root
        while root:
            if value > root.value:
                answer = root
                root = root.right
            else:
                root = root.left
        return answer

    def delete(self, value):
        pass

tree = BinSearchTree()

for line in f_in.readlines():
    line = line.strip().split()
    if line[0] == "insert":
        tree.insert(line[1])
    
    if line[0] == "exists":
        print(tree.exists(line[1]))

    if line[0] == "next":
        answer = tree.next(line[1])
        if answer:
            print(answer.value)
        else:
            print("none")

    if line[0] == "prev":
        answer = tree.prev(line[1])
        if answer:
            print(answer.value)
        else:
            print("none")
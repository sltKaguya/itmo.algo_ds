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
                else:
                    return

    def search(self, value):
        root = self.root
        while root:
            if value == root.value:
                return root
            elif value > root.value:
                root = root.right
            else:
                root = root.left

    def exists(self, value):
        if self.search(value):
            return "true\n"
        else:
            return "false\n"

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
        node = self.search(value)
        if not node:
            return
        parent = node.parent
        if not(node.left) and not(node.right):
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        
        elif node.left and node.right:
            successor = self.next(value)
            node.value = successor.value
            if successor.parent:
                if successor.parent.left == successor:
                    successor.parent.left = successor.right
                    if successor.right:
                        successor.right.parent = successor.parent
                else:
                    successor.parent.right = successor.right
                    if successor.right:
                        successor.right.parent = successor.parent
            else:
                self.root = successor.right
                if successor.right:
                    successor.right.parent = None
        
        else:
            if node.left:
                if not(parent):
                    self.root = node.left
                    node.left.parent = None
                elif parent.left == node:
                    parent.left = node.left
                    node.left.parent = parent
                else:
                    parent.right = node.left
                    node.left.parent = parent
            else:
                if not(parent):
                    self.root = node.right
                    node.right.parent = None
                elif parent.left == node:
                    parent.left = node.right
                    node.right.parent = parent
                else:
                    parent.right = node.right
                    node.right.parent = parent
        
tree = BinSearchTree()
ans_string = ""
for line in f_in.readlines():
    line = line.strip().split()
    if line[0] == "insert":
        tree.insert(int(line[1]))
    
    if line[0] == "exists":
        ans_string += tree.exists(int(line[1]))

    if line[0] == "next":
        answer = tree.next(int(line[1]))
        if answer:
            ans_string += str(answer.value) + "\n"
        else:
            ans_string += ("none") + "\n"

    if line[0] == "prev":
        answer = tree.prev(int(line[1]))
        if answer:
            ans_string += str(answer.value) + "\n"
        else:
            ans_string += "none\n"

    if line[0] == "delete":
        tree.delete(int(line[1]))

ans_string = ans_string.strip()
#print(ans_string)
f_out.write(ans_string)
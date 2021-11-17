class Node():

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree():

    def __init__(self):
        self.root = None

    def create_node(self, array, index):
        if index != -1:
            elem = Node(array[index][0])
            elem.left = self.create_node(array, array[index][1] - 1)
            elem.right = self.create_node(array, array[index][2] - 1)
            return elem
        else: 
            return None

    def height(self, root):
        if root:
            return max(self.height(root.right), self.height(root.left)) + 1
        else:
            return 0

f_in = open("height.in")
f_out = open("height.out", "w")

n = int(f_in.readline().strip())
tree = BinaryTree()
array = []

for i in range(n):
    line = f_in.readline().split()
    temp_array = []
    for y in range(3):
        temp_array.append(int(line[y]))
    array.append(temp_array)
if len(array) != 0:
    tree.root = Node(array[0][0])
    tree.root.left = tree.create_node(array, array[0][1] - 1)
    tree.root.right = tree.create_node(array, array[0][2] - 1)

print(tree.height(tree.root), file=f_out)
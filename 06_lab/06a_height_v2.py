f_in = open("height.in")
f_out = open("height.out", "w")

n = int(f_in.readline().strip())
tree = []
max_height = 0
for i in range(n):
    array = []
    line = [int(i) for i in f_in.readline().split()]
    array += line
    array.append(1)
    tree.append(array)  

for elem in tree:
    if elem[1] != 0:
        tree[elem[1] - 1][3] += elem[3]
    if elem[2] != 0:
        tree[elem[2] - 1][3] += elem[3] 
    if elem[3] > max_height:
        max_height = elem[3]

f_out.write(str(max_height))
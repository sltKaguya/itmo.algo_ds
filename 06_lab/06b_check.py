f_in = open("check.in")
f_out = open("check.out", "w")

n = int(f_in.readline().strip())
tree = []
for i in range(n):
    array = [int(i) for i in f_in.readline().split()]
    array += [-(10**10), 10**10]
    tree.append(array)

if n == 0:
    f_out.write("YES")
    quit()

flag = True
for elem in tree:
    if elem[1] != 0:
        tree[elem[1] - 1][3] = elem[3]
        tree[elem[1] - 1][4] = elem[0]

    if elem[2] != 0:
        tree[elem[2] - 1][3] = elem[0]
        tree[elem[2] - 1][4] = elem[4]

    if (elem[0] <= elem[3]) or (elem[0] >= elem[4]):
        flag = False
        break

if flag:
    f_out.write("YES")
else:
    f_out.write("NO")

print(tree)
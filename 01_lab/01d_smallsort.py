fin = open("smallsort.in")
fout = open("smallsort.out", "w")

n = int(fin.readline().strip())
Sort = [int(i) for i in fin.readline().split()]

for i in range(n, 1, -1):
    for j in range(i - 1):
        if Sort[j] > Sort[j + 1]:
            Sort[j], Sort[j + 1] = Sort[j + 1], Sort[j]

string = ''
ln = len(Sort)
for i in range(ln):
    if i < ln - 1:
        string += '{} '.format(Sort[i])
    else:
        string += '{}'.format(Sort[i])

print(string, file=fout)
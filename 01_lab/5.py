fin = open("sortland.in")
fout = open("sortland.out", "w")

n = int(fin.readline().strip())

Non_sorted = [float(i) for i in fin.readline().split()]

Sorted = []
for elem in Non_sorted:
    Sorted.append(elem)

for i in range(n, 1, -1):
    for j in range(i - 1):
        if Sorted[j] > Sorted[j + 1]:
            Sorted[j], Sorted[j + 1] = Sorted[j + 1], Sorted[j]

ans = ""
for x in range(len(Non_sorted)):
    if Non_sorted[x] == Sorted[0]:
        poor = x + 1
    elif Non_sorted[x] == Sorted[(n - 1) // 2]:
        mid = x + 1
    elif Non_sorted[x] == Sorted[n - 1]:
        rich = x + 1

ans += "{} {} {}".format(poor, mid, rich)
print(ans, file=fout)
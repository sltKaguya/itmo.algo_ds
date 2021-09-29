f_in = open("inversions.in")
f_out = open("inversions.out")

n = int(f_in.readline().strip())

Num = [int(i) for i in f_in.readline().split()]

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        print(Num[i], Num[j])
        if Num[i] > Num[j]:
            count += 1
            print("yis")

print(count, file=f_out)
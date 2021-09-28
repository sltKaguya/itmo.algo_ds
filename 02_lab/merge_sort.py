f_in = open("sort.in")
f_out = open("sort.out", "w")
   
n = f_in.readline().strip()
A = [int(i) for i in f_in.readline().split()]
B = []
for elem in A:
    B.append([elem])

while len(B) != 1:
    print(B)
    B.pop(0)
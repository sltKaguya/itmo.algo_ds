fin = open("aplusbb.in")
fout = open("aplusbb.out", "w")

a, b = map(int, fin.readline().split())
print(a + b ** 2, file=fout)

fout.close()
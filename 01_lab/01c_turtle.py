fin = open("turtle.in")
fout = open("turtle.out", "w")

h, w = list(map(int, fin.readline().split()))

matrix = list(list(map(int, fin.readline().split())) for i in range(h))

for i in range(h - 1, -1, -1):
    for j in range(w):
        if i == h - 1:
            if j != 0:
                matrix[i][j] += matrix[i][j-1]
        else:
            if j == 0:
                matrix[i][j] += matrix[i + 1][j]
            else: 
                matrix[i][j] += max(matrix[i][j - 1], matrix[i + 1][j]) 
        
print(matrix[0][w - 1], file=fout)

fout.close()
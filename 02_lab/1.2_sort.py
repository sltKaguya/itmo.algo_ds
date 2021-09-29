f_in = open("sort.in")
f_out = open("sort.out", "w")

n = f_in.readline().strip()
A = [[int(i)] for i in f_in.readline().split(" ")]
B = A
while len(A) != 1:
    A = B
    i = j = 0

    while i < len(A[1]) and j < len(A[2]):
        k = 0
        if A[1][i] < A[2][j]:
            B[1][k] = A[1][i]
            i += 1
        else:
            B[1][k] = A[2][j]
            j += 1
        k += 1

    while i < len(A[1]):
            B[1][k] = A[1][k]
            i += 1
            k += 1

    while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

print(B)
f_in = open("sort.in")
f_out = open("sort.out", "w")

def merge(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        merge(L)
        merge(R)
        i, j, k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            A[k] = L[i]
            k += 1

        while j < len(R):
            A[k] = R[j]
            k += 1
   
n = f_in.readline().strip()
A = [int(i) for i in f_in.readline().split()]

print(merge(A))
#B = []
#for elem in A:
#    B.append([elem])

#while len(B) != 1:
#    print(B)
#    B.pop(0)
f_in = open("inversions.in")
f_out = open("inversions.out", "w")

def msort(A):
    if len(A) > 1:
        mid = A // 2
        L = A[:mid]
        R = A[mid:]

        msort(L)
        msort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
                k += 1
                count += 1
            else:
                A[k] = R[j]
                j += 1
                k +=1
        while i < len(L):
            A[k] = L[i]
            i += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
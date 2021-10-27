f_in = open("antiqs.in")
f_out = open("antiqs.out", "w")

def antiqsort(arr):
    for i in range(len(arr)):
        arr[i], arr[i // 2] = arr[i // 2], arr[i]
    return arr

n = int(f_in.readline().strip())
a = [i for i in range(1, n + 1)]

f_out.write(" ".join([str(i) for i in antiqsort(a)]))
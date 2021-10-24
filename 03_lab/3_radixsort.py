f_in = open("radixsort.in")
f_out = open("radisort.out", "w")

def quicksort(arr):
    

n, m, k = map(int, f_in.readline().split())
array = []
for i in range(n):
    array.append(f_in.readline().strip())

print(n, m, k)
print(array)
f_in = open("isheap.in")
f_out = open("isheap.out", "w")

def check_heap(arr):
    result = "YES"
    for i in range(1, len(arr)):
        index = i
        while index != 0:
            parent = (index - 1) // 2
            if arr[index] >= arr[parent]:
                break
            result = "NO"
            break
    return result

n = int(f_in.readline().strip())
a = [int(i) for i in f_in.readline().split()]

res = check_heap(a)
f_out.write(res)
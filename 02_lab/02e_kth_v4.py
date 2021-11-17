f_in = open("kth.in")
f_out = open("kth.out", "w")

n, k = map(int, f_in.readline().split())
a, b, c, a_1, a_2 = map(int, f_in.readline().split())

my_arr = [a_1, a_2]
bit_32 = 2 ** 32 - 1
bit_31 = 2 ** 31

def overflow(num):
    a = num & bit_32
    if a & bit_31 > 0:
        return a - bit_32 - 1
    return a

def partition(arr, left, right):
    pivot = arr[len(arr) // 2]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return j

def find_k(arr, k):
    left = 0
    right = len(arr) - 1
    while True:
        mid = partition(arr, left, right)

        if k == mid:
            return arr[mid]
        
        elif k < mid:
            right = mid
        else:
            left = mid + 1

for i in range(2, n):
    my_arr.append(overflow(overflow(a * my_arr[i - 2]) +
                    overflow(b * my_arr[i - 1]) + c
                ))

print(find_k(my_arr, k))
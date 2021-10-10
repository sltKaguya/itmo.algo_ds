import random

f_in = open("kth.in")
f_out = open("kth.out", "w")

def overflow(num):
    a = num & 2 ** 32 - 1
    if a & 2 ** 31 > 0:
        return a - (2 ** 32 - 1)
    return a
        
def split_arr(arr):
    left = separator_1 = separator_2 = 0
    right = len(arr) - 1
    rand_indx = random.randint(0, len(arr) - 1)
    pivot = arr[rand_indx]

    for i in range(left, right - 1):
        if arr[i] < pivot:
            arr[separator_1], arr[separator_2], arr[i] = \
                arr[i], arr[separator_1], arr[separator_2]
            separator_1 += 1
            separator_2 += 1
        elif arr[i] == pivot:
            arr[separator_2], arr[i] = arr[i], arr[separator_2]
            separator_2 += 1
    return(arr, separator_1, separator_2)

def kth_qsort(arr):
    if len(arr) < 2:
        return arr
    arr, sep_1, sep_2 = split_arr(arr)
    left_part = kth_qsort(arr[:sep_1])
    right_part = kth_qsort(arr[sep_2:])
    return left_part + arr[sep_1:sep_2] + right_part

n, k = map(int, f_in.readline().split())
a, b, c, a_1, a_2 = map(int, f_in.readline().split())
arr = [a_1, a_2]
for i in range(2, n):
    arr.append(i)
    #arr.append(overflow(overflow(a * arr[i - 2]) + overflow(b * arr[i - 1]) + c))

print(arr)
print(kth_qsort(arr))
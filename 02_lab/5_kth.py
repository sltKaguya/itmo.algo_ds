import random

f_in = open("kth.in")
f_out = open("kth.out", "w")

bit_32 = 2 ** 32 - 1
bit_31 = 2 ** 31

def overflow(number):
    a = number & bit_32
    if a & bit_31 > 0:
        return a - bit_32 - 1
    return a

def qsort_kth(arr, left, right, k):
    if (right - left) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    l_ind, r_ind = left, right - 1
        
    while l_ind <= r_ind:
        while arr[l_ind] < pivot:
                l_ind += 1

        while arr[r_ind] > pivot:
                r_ind -= 1
            
        if l_ind <= r_ind:
                arr[l_ind], arr[r_ind] = arr[r_ind], arr[l_ind]
                l_ind += 1
                r_ind -= 1

    if k <= r_ind:
        return qsort_kth(arr, left, r_ind, k)
    else:
        return qsort_kth(arr, l_ind, right, k)

n, k = map(int, f_in.readline().split())

frst, scnd, thrd, a_1, a_2 = map(int, f_in.readline().split())
arr = [0] * n
arr[0], arr[1] = a_1, a_2
for i in range(2, n):
    arr[i] = overflow(overflow(frst * arr[i - 2]) + overflow(scnd * arr[i - 1]) + thrd)
print(str(qsort_kth(arr, 0, len(arr), k)[k - 1]))
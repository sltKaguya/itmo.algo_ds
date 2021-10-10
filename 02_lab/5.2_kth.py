import random

f_in = open('kth.in')
f_out = open('kth.out', 'w')

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

def kth(arr, left, right, k):
    if left >= right:
        return arr
    else:
        pivot = arr[random.randint(0, right)]
        l_ind, r_ind = left, right
        
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
            return kth(arr, left, r_ind, k)
        else:
            return kth(arr, l_ind, right, k)

for i in range(2, n):
    my_arr.append(overflow(overflow(a * my_arr[i - 2]) +
                    overflow(b * my_arr[i - 1]) + c
                ))

f_out.write(str(kth(my_arr, 0, len(my_arr) - 1, k - 1)[k - 1]))
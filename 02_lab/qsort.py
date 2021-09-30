import random

def qsort(Arr):
    if len(Arr) < 2:
        return Arr
    else:
        rand_ind = random.randint(0, len(Arr) - 1)
        pivot = Arr[rand_ind]
        Arr.pop(rand_ind)
        left = [i for i in Arr if i < pivot]
        right = [i for i in Arr if i >= pivot]

        Sorted_arr = qsort(left) + [pivot] + qsort(right)
        return Sorted_arr


A = [1477, 4, 3, 2328, 234384, 3487, 24737, 42, 38]
print(qsort(A))
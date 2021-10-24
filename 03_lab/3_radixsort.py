f_in = open("radixsort.in")
f_out = open("radixsort.out", "w")

def quicksort(arr, k):
    if len(arr) < 2:
        return arr
    mid_index = (len(arr) // 2)
    pivot = arr[mid_index]
    arr.pop(mid_index)

    left = []
    right = []
    for index in range(len(arr)):
        i = arr[index]
        if i[k] < pivot[k]:
            left.append(i)
        elif i[k] > pivot[k]:
            right.append(i)
        else:
            if index < mid_index:
                left.append(i)
            else:
                right.append(i)
    sorted_Arr = quicksort(left, k) + [pivot] + quicksort(right, k)
    return sorted_Arr

def radixsort(arr, m, k):
    result = arr
    for i in range(k):
        result = quicksort(result, m - i - 1)
    return result

n, m, k = map(int, f_in.readline().split())
array = []
for i in range(n):
    array.append(f_in.readline().strip())

f_out.write("\n".join(radixsort(array, m, k)))
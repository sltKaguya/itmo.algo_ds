f_in = open("inversions.in")
f_out = open("inversions.out", "w")

def msort_inversions(arr):
    inversions = 0
    if len(arr) == 1:
        return arr, 0
    else:
        mid = arr // 2
        left = arr[:mid]
        right = arr[mid:]

        left, left_inversions = msort_inversions(left)
        right, right_inversions = msort_inversions(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k +=1
                inversions += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            inversions += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
    return inversions

n = int(f_in.readline().strip())

unsorted_arr = [int(i) for i in f_in.readline().split()]
print(msort_inversions(unsorted_arr))

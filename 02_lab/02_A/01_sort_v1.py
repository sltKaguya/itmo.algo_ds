f_in = open("sort.in")
f_out = open("sort.out", "w")

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
   
n = f_in.readline().strip()
arr = [int(i) for i in f_in.readline().split()]

merge(arr)
print(" ".join([str(elem) for elem in arr]), file=f_out)
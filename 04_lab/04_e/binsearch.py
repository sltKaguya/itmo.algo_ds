f_in = open("binsearch.in")
f_out = open("binsearch.out", "w")

def binsearch_left(key, arr):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] > key:
            left = mid
        else:
            right = mid
    if right < len(arr) and arr[right] == key:
        return left
    else:
        return "-1 -1"
def binsearch_right(key, arr):
    left = -1
    right = len(arr)
    while right > left + 1:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid
        else:
            left = mid
    if left >= 0 and arr[left] == key:
        return left
    else:
        return "-1 -1"
        
n = int(f_in.readline().strip())
array = [int(i) for i in f_in.readline().split()]
m = int(f_in.readline().strip())
searchnum = [int(i) for i in f_in.readline().split()]

print(n, array, m, searchnum)
print(binsearch_left(1, array))
print(binsearch_right(1, array))
f_in = open("binsearch.in")
f_out = open("binsearch.out", "w")

def binsearch_left(key, arr):
    result = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            result = mid
            right = mid - 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return result

def binsearch_right(key, arr):
    result = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            result = mid
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return result
        
n = int(f_in.readline().strip())
array = [int(i) for i in f_in.readline().split()]
m = int(f_in.readline().strip())
searchnum = [int(i) for i in f_in.readline().split()]
answers = []
for i in range(m):
    left_index = binsearch_left(searchnum[i], array)
    right_index = binsearch_right(searchnum[i], array)
    if left_index >= 0:
        left_index += 1
        right_index += 1
    answers.append(f"{left_index} {right_index}")

f_out.write("\n".join(answers))

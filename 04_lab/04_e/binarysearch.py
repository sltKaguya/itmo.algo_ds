def binsearch(key, arr):
    result = -1
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == key:
            result = mid
            break
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return result
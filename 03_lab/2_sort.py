f_in = open("sort.in")
f_out = open("sort.out", "w")

f_in.readline()
a = [int(i) for i in f_in.readline().split()]

def make_heap(arr):
    for i in range(1, len(arr)):
        index = i
        while index != 0:
            parent = (index - 1) // 2
            if arr[index] <= arr[parent]:
                break
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
    return arr

def heap_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        index = 0
        while True:
            child_1 = index * 2 + 1
            child_2 = index * 2 + 2
            if child_1 >= i:
                child_1 = index
            if child_2 >= i:
                child_2 = index
            if arr[index] >= arr[child_1] and arr[index] >= arr[child_2]:
                break
            if arr[child_1] > arr[child_2]:
                child_big = child_1 
            else:
                child_big = child_2
            arr[index], arr[child_big] = arr[child_big], arr[index]
            index = child_big
    return arr

a_sorted = heap_sort(make_heap(a))
f_out.write(" ".join(str(i) for i in a_sorted))
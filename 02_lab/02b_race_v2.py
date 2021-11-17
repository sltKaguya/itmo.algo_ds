f_in = open("race.in")
f_out = open("race.out", "w")

def merge_sort (arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                arr[k] = left[i]
                i += 1
                k += 1
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

n = int(f_in.readline().strip())
my_arr = []
for i in range(n):
    my_arr.append(f_in.readline().split())

merge_sort(my_arr)
ans = "=== " + my_arr[0][0] + " ===\n" + my_arr[0][1]
for i in range(1, len(my_arr)):
    if my_arr[i][0] != my_arr[i - 1][0]:
        ans += "\n=== " + my_arr[i][0] + " ==="
    ans += "\n" + my_arr[i][1]
print(ans, file=f_out)
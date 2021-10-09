f_in = open("race.in")
f_out = open("race.out", "w")

def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].split()[0] <= right[j].split()[0]:
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

n = int(f_in.readline().strip())
my_arr = []
for i in range(n):
    my_arr.append(f_in.readline().strip())

merge_sort(my_arr)

country = my_arr[0][:my_arr[0].find(" ")]
ans = "=== " + my_arr[0][:my_arr[0].find(" ")] + " ===\n" + \
    my_arr[0][my_arr[0].find(" ") + 1:]
for i in range(1, n):
    if my_arr[i][:my_arr[i].find(" ")] != country:
        country = my_arr[i][:my_arr[i].find(" ")]
        ans += "\n=== " + my_arr[i][:my_arr[i].find(" ")] + " ==="
    ans += "\n" + my_arr[i][my_arr[i].find(" ") + 1:]
print(ans, file=f_out)
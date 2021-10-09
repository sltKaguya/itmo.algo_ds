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
            if (left[i][:left[i].find(" ")]) <= (right[j][:right[j].find(" ")]):
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

n = int(f_in.readline())
my_arr = []
for i in range(n):
    my_arr.append(f_in.readline().strip())

merge_sort(my_arr)
country_check = ""
for i in range(n):
    country = my_arr[i][:my_arr[i].find(" ")]
    if country != country_check:
        country_check = country
        f_out.write("=== " + country + " ===\n")
    f_out.write(my_arr[i][my_arr[i].find(" ") + 1:] + "\n")
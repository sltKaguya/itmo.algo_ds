import random

f_in = open("race.in")
f_out = open("race.out", "w")

def qsort(Arr):
    if len(Arr) < 2:
        return Arr
    rand_index = random.randint(0, len(Arr) - 1)
    pivot = Arr[rand_index]
    Arr.pop(rand_index)

    Left = [i for i in Arr if i < pivot]
    Right = [i for i in Arr if i >= pivot]

    Sorted_Arr = qsort(Left) + [pivot] + qsort(Right)
    return Sorted_Arr

n = int(f_in.readline().strip())
lines = f_in.read().splitlines()
Unsorted_dic = {}
for line in lines:
    key, value = line.split()
    if key not in Unsorted_dic:
        Unsorted_dic[key] = [value]
    else:
        Unsorted_dic[key] += [value]

Sorted_keys = qsort(list(Unsorted_dic.keys()))

a = ""
for elem in Sorted_keys:
    if a == "":
        a += "=== " + elem + " ===\n"
    else:
        a += "\n=== " + elem + " ===\n"
    a += '\n'.join([i for i in Unsorted_dic[elem]])

print(a, file=f_out)
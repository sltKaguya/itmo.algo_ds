import random
#from typing import List

f_in = open("race.in", "r")
f_out = open("race.out", "w")

def partition(Keys_arr, low, high):
    i = low - 1
    pivot = Keys_arr[high]
    for j in range(low, high):
        if Keys_arr[j] <= Keys_arr[pivot]:
            i += 1
            Keys_arr[i], Keys_arr[j] = Keys_arr[j], Keys_arr[i]
    
    Keys_arr[i + 1], Keys_arr[high] = Keys_arr[high], Keys_arr[i + 1]

    return i + 1

def qsort(Dic, low, high):
    Keys_arr = list(dict.keys(Dic))
    if low < high:
        pivot = partition(Keys_arr, low, high)
        qsort(Keys_arr, low, pivot - 1)
        qsort(Keys_arr, pivot + 1 , high)

n = int(f_in.readline().strip())
lines = f_in.read().splitlines()
Cntr_runn = {}
for line in lines:
    key, value = line.split()
    if key not in Cntr_runn:
        Cntr_runn.update({key: value})
    else:
        Cntr_runn[key] += " " + value

print(Cntr_runn)
qsort(Cntr_runn, 0, len(Cntr_runn) - 1)
#qsort(Cntr_runn, 0, len(Cntr_runn) - 1)
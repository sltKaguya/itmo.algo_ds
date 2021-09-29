import random
#from typing import List

f_in = open("race.in", "r")
f_out = open("race.out", "w")

def partition(Dic, low, high):
    Arr = list(dict.keys(Dic))
    i = low - 1
    pivot = Arr[high]
    for j in range(low, high):
        if Arr[j] <= Arr[pivot]:
            i += 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
    
    Arr[i + 1], Arr[high] = Arr[high], Arr[i + 1]

    return i + 1

def qsort(Dic, low, high):
    Arr = list(dict.keys(Dic))
    if low < high:
        pivot = partition(Arr, low, high)
        qsort(Arr, low, pivot - 1)
        qsort(Arr, pivot + 1 , high)

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
#qsort(Cntr_runn, 0, len(Cntr_runn) - 1)
qsort(Cntr_runn, 0, len(Cntr_runn) - 1)
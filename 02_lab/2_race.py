from os import readlink


f_in = open("race.in", "r")
f_out = open("race.out", "w")

n = f_in.readline().strip()
lines = f_in.read().splitlines()
A = {}
for line in lines:
    key, value = line.split()
    if key not in A:
        A.update({key: value})
    else:
        A[key] += " " + value

print(A)
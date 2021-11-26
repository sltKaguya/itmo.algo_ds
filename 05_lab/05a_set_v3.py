f_in = open("set.in")
f_out = open("set.out", "w")

size = 100
commands = [i.strip().split() for i in f_in.readlines()]
hash_table = [[] for i in range(size)]

for command in commands:
    index = int(command[1]) % size
    value = int(command[1])

    if command[0] == "insert":
        check = True
        for elem in hash_table[index]:
            if elem == value:
                check = False
        if check:
            hash_table[index].append(value)

    elif command[0] == "exists":
        check = False
        for elem in hash_table[index]:
            if elem == value:
                check = True
                break
        print("ftarlusee"[check::2], file=f_out)
                
    else:
        for ind, elem in enumerate(hash_table[index]):
            if elem == value:
                hash_table[index].pop(ind)
                break

print(hash_table)
f_out.close()
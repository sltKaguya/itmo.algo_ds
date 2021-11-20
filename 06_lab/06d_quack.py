f_in = open("quack.in")
f_out = open("quack.out", "w")

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():

    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, value):
        elem = Node(value)
        if not self.first:
            self.first = elem
            self.last = elem
        else:
            self.last.next = elem
            self.last = elem

    def extract(self):
        value = self.first.value
        self.first = self.first.next
        return value

def get_asc(string):
    return ord(string) - 97

lines = [i for i in f_in.read().split()]
queue = Queue()
lenght = len(lines)
index = 0
const = 65536
mod_c = 256
register = [0]*26
results = []
str_keys = {}

while index < lenght:
    if lines[index].isdigit():
        queue.insert(int(lines[index]))

    elif lines[index][0] == "+":
        x = queue.extract()
        y = queue.extract()
        queue.insert((x + y) % const)

    elif lines[index][0] == "-":
        x = queue.extract()
        y = queue.extract()
        queue.insert((x - y) % const)

    elif lines[index][0] == "*":
        x = queue.extract()
        y = queue.extract()
        queue.insert((x * y) % const)

    elif lines[index][0] == "/":
        x = queue.extract()
        y = queue.extract()
        if not y:
            queue.insert((x // y) % const)
        else:
            queue.insert(0)

    elif lines[index][0] == "%":
        x = queue.extract()
        y = queue.extract()
        if not y:
            queue.insert((x % y) % const)
        else:
            queue.insert(0)

    elif lines[index][0] == ">":
        x = queue.extract()
        register[get_asc(lines[index][1:])] = x

    elif lines[index][0] == "<":
        queue.insert(register[get_asc(lines[index][1:])])

    elif lines[index][0] == "P":
        if len(lines[index]) == 1:
            results.append(str(queue.extract()) + "\n")
        else:
            results.append(str(register[get_asc(lines[index][1:])]) + "\n")

    elif lines[index][0] == "C":
        if len(lines[index]) == 1:
            results.append(chr(queue.extract() % mod_c))
        else:
            results.append(chr(register[get_asc(lines[index][1:])] % mod_c))

    elif lines[index][0] == ":":
        str_keys[lines[index][1:]] = index

    elif lines[index][0] == "J":
        if not(lines[index][1:] in str_keys):
            str_keys[lines[index][1:]] = lines.index(":" + lines[index][1:])
            
        index = str_keys[lines[index][1:]] - 1
        
    elif lines[index][0] == "Z":
        if not(lines[index][2:] in str_keys):
            str_keys[lines[index][2:]] = lines.index(":" + lines[index][2:])
        
        if register[get_asc(lines[index][1])] == 0: 
                index = str_keys[lines[index][2:]] - 1  
    
    elif lines[index][0] == "E":
        if not(lines[index][3:] in str_keys):
            str_keys[lines[index][1:]] = lines.index(":" + lines[index][3:])
        
        if register[get_asc(lines[index][1])] == \
                register[get_asc(lines[index][2])]:
            index = str_keys[lines[index][3:]] - 1

    elif lines[index][0] == "G":
        if not(lines[index][3:] in str_keys):
            str_keys[lines[index][1:]] = lines.index(":" + lines[index][3:])
        
        if register[get_asc(lines[index][1])] > \
                register[get_asc(lines[index][2])]:
            index = str_keys[lines[index][3:]] - 1

    elif lines[index][0] == "Q":
        f_out.write("".join(results))
        quit()
            
    index += 1

f_out.write("".join(results))
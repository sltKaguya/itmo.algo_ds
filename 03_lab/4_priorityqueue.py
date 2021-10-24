f_in = open("priorityqueue.in")
f_out = open("priorityqueue.out", "w")

def push(heap, pair):
    if len(heap) == 0:
        heap.append(pair)
    elif len(heap) == 1:
        heap.append(pair)
        if heap[0][0] > heap[1][0]:
            heap[1], heap[0] = heap[0], heap[1]
    else:
        heap.append(pair)
        index = len(heap) - 1
        parent = (index - 1) // 2
        while (heap[index][0] < heap[parent][0]) and parent >= 0:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
            parent = (index - 1) // 2
    
    return heap

def extract_min(heap):
    if len(heap) < 1:
        return heap, "*"
    else:
        result = str(heap[0][0])
        heap[0] = heap[len(heap) - 1]
        heap = heap[:len(heap) - 1]
        if len(heap) > 0:
            index = 0
            count = len(heap) - 1
            while True:
                child_1 = 2 * index + 1
                child_2 = 2 * index + 2

                if child_1 > count:
                    child_1 = index
                if child_2 > count:
                    child_2 = index
                if heap[index][0] <= heap[child_1][0] and heap[index][0] <= heap [child_2][0]:
                    break

                if heap[child_1][0] < heap[child_2][0]:
                    swap_child = child_1
                else:
                    swap_child = child_2
                heap[index], heap[swap_child] = heap[swap_child], heap[index]
                index = swap_child
    return heap, result

def decrease_key(heap, x, y):
    index = 0
    for i in range(len(heap)):
        if heap[i][1] == x - 1:
            heap[i][0] = y
            index = i
            break
    
    if len(heap) > 1:
        parent = (index - 1) // 2
        while heap[index][0] < heap[parent][0]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
            parent = (index - 1) // 2

    return heap

commands = f_in.read().split("\n")
results = []
heap = []

for index, elem in enumerate(commands):
    if elem.startswith("push"):
        heap = push(heap, [int(elem.split()[1]), index])
    elif elem.startswith("extract-min"):
        heap, result = extract_min(heap)
        results.append(result)
    else:
        heap = decrease_key(heap, int(elem.split()[1]), int(elem.split()[2]))

f_out.write("\n".join(results))
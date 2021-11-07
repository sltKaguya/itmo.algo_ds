f_in = open("garland.in")
f_out = open("garland.out", "w")

def search_last(left, right, first, lenght):
    elem = (left + right) / 2
    array = [first, elem]
    minimal = first
    for i in range(2, lenght):
        new_elem = array[i-1] * 2 - array[i-2] + 2
        if new_elem < minimal:
            minimal = new_elem
        array.append(new_elem)
    if abs(minimal) < 0.00001:
        return array[lenght - 1]
    elif minimal < 0:
        return search_last(elem, right, first, lenght)
    else:
        return search_last(left, elem, first, lenght)
    
n, first = map(float, f_in.readline().split())

f_out.write(str("%.2f" % (search_last(0, first, first, int(n)))))
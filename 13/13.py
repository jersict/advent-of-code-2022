
def evaluateOrder(one, two):
    if isinstance(one, int) and isinstance(two, int):
        if one < two:
            return True
        elif two < one:
            return False
        return None
    elif isinstance(one, int):
        return evaluateOrder([one], two)
    elif isinstance(two, int):
        return evaluateOrder(one, [two])
    else:
        for i in range(len(one)):
            if i > len(two)-1:
                return False
            order = evaluateOrder(one[i], two[i])
            if order != None:
                return order
            else:
                continue
        if len(two) > len(one):
            return True
        return None

def sort(sorted):
    for i in range(int(len(sorted)/2)):
        for val in sorted[i+1]:
            inserted = False
            for j, v in enumerate(sorted[i]):
                if evaluateOrder(val, v):
                    sorted[i].insert(j, val)
                    inserted = True
                    break
            if not inserted:
                sorted[i].append(val)
        sorted.pop(i+1)
    return sorted



if __name__ == "__main__":
    with open("13/input.txt") as file:
        lines = file.readlines()
        sumP1 = 0
        sorted = []
        for i in range(int(len(lines)/3)):
            one = eval(lines[i*3].strip())
            two = eval(lines[i*3+1].strip())
            if evaluateOrder(one, two):
                sumP1 += i + 1
                sorted.append([one, two])
            else:
                sorted.append([two, one])
        sorted.append([[[2]],[[6]]])
        while len(sorted) > 1:
            sorted = sort(sorted)
        i1 = sorted[0].index([[2]])+1
        i2 = sorted[0].index([[6]])+1
        print('Sum of indices in right order is {0}.\n When sorted [[2]] is at index {1}, while [[6]] is at index {2}.\n Indexes multiplied together makes us to {3}'.format(sumP1, i1, i2, i1*i2))
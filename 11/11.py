class Monkey:
    def __init__(self, items, op, test, ifTrue, ifFalse):
        self.items = items
        self.op = op
        self.test = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse

    def recieve(self, item):
        self.items.append(item)

    def inspect(self):
        self.items[0] = self.op(self.items[0])
        self.items[0] %= 9699690 

    def throw(self):
        if self.items[0] % self.test == 0:
            return self.items.pop(0), self.ifTrue
        else:
            return self.items.pop(0), self.ifFalse


def createMonkeys(lines):
    monkeys = []
    inspections = []
    items = []
    ops = [m0, m1, m2, m3, m4, m5, m6, m7]
    i = 0
    for line in lines:
        if 'Starting items' in line:
            items = [eval(i) for i in line.split(': ')[1].split(', ')]
        elif 'Operation' in line:
            operation = line.split('= ')[1].split(' ')
        elif 'Test:' in line:
            test = int(line.split('by ')[1])
        elif 'true: ' in line:
            ifTrue = int(line.split('monkey ')[1])
        elif 'false: ' in line:
            ifFalse = int(line.split('monkey ')[1])
        elif line == '\n':
            inspections.append(0)
            monkeys.append(Monkey(items, ops[i], test, ifTrue, ifFalse))
            i += 1
    return monkeys, inspections


def m0(x):
    return x * 17

def m1(x):
    return x + 5

def m2(x):
    return x + 8

def m3(x):
    return x + 1

def m4(x):
    return x + 4

def m5(x):
    return x * 7

def m6(x):
    return x + 6

def m7(x):
    return x * x

if __name__ == "__main__":
    with open("11/input.txt") as file:
        lines = file.readlines()
        monkeys, inspections = createMonkeys(lines)
        for round in range(10000):
            for i, monkey in enumerate(monkeys):
                while len(monkey.items) > 0:
                    monkey.inspect()
                    inspections[i] += 1
                    item, target = monkey.throw()
                    monkeys[target].recieve(item)
        print('Level of monkey business is {0}'.format(sorted(inspections)[-1]*sorted(inspections)[-2]))
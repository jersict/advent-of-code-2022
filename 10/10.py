if __name__ == "__main__":
    with open("10/input.txt") as file:
        screen = ''
        x = 1
        stops = [20, 60, 100, 140, 180, 220]
        newline = [40, 80, 120, 160, 200, 240]
        signals = 0
        op = 'noop'
        program = file.readlines()
        for cycle in range(1, 241):
            if cycle in newline:
                screen += '\n'
            elif abs(cycle%40-1 - x) < 2:
                screen += '#'
            else:
                screen += '.'
            if cycle in stops:
                signals += cycle*x
            if op == 'noop':
                op = program.pop(0).strip()
                continue
            else:
                x += int(op.split(' ')[1])
                op = 'noop' 
        print('Sum of the six signals is {0}'.format(signals))
        print(screen)
import copy

def prepareStacksAndMoves():
    stacks = []
    with open("05/input.txt") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line[:3] == ' 1 ':
                return stacks, lines[i+2:]
            else:
                crates = [line[i:i+4] for i in range(0, len(line), 4)]
                for i, crate in enumerate(crates):
                    if len(stacks) == i:
                        stacks.append([])
                    if crate != ('    ' or '    \n'):
                        stacks[i].append(crate.strip())

def crateMover9000(stacks, moves):
    for move in moves:
        vals = move.strip().split(' ')
        ammount = int(vals[1])
        frm = int(vals[3])-1
        to = int(vals[5])-1
        for i in range(ammount):
            crate = stacks[frm].pop(0)
            stacks[to].insert(0, crate)
    return stacks

def crateMover9001(stacks, moves):
    for move in moves:
        vals = move.strip().split(' ')
        ammount = int(vals[1])
        frm = int(vals[3])-1
        to = int(vals[5])-1
        crates = stacks[frm][:ammount]
        for i in range(ammount):
            stacks[frm].pop(0)
        stacks[to] = crates + stacks[to]
    return stacks

if __name__ == "__main__":
    stacks, moves = prepareStacksAndMoves()
    stacks9000 = crateMover9000(copy.deepcopy(stacks), moves)
    stacks9001 = crateMover9001(stacks, moves)
    r9000 = ''
    for stack in stacks9000:
        r9000 += stack[0][1]
    r9001 = ''
    for stack in stacks9001:
        r9001 += stack[0][1]
    print('Top crates are {0} for CrateMover 9000, and {1} for CrateMover 9001'.format(r9000, r9001))
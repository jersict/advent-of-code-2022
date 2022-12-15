def populateDir(dir, instructions):
    path = []
    i=0
    currentDir = []
    for line in instructions:
        i+=1
        if len(instructions) == 0:
            break
        line = line.strip().replace('$ ','')
        if line == 'cd /':
            dir['/'] = {}
            path.append('/')
            currentDir = dir['/']
        else:
            instr = line.split(' ') 
            if instr[0] == 'cd' and instr[1] != '..':
                path.append(instr[1])
                currentDir = currentDir[instr[1]]
            elif instr[0] == 'cd' and instr[1] == '..':
                path.pop(-1)
                currentDir = dir
                for p in path:
                    currentDir = currentDir[p]
            elif line == 'ls':
                continue
            elif instr[0] == 'dir':
                currentDir[instr[1]]={}
            else:
                currentDir[instr[1]]=int(instr[0])
    return dir

def measure(dir, s, sizes):
    if not all(isinstance(x, int) for x in list(dir.values())):
        for key in list(dir.keys()):
            if not(isinstance(dir[key], int)):
                dir[key], s , sizes = measure(dir[key], s, sizes)
    size = sum(list(dir.values()))
    sizes.append(size)
    if size < 100000:
        s += size
    return size, s, sizes 

if __name__ == "__main__":
    with open("07/input.txt") as file:
        dir = {}
        lines = file.readlines()
        dir= populateDir(dir, lines)
        dir, s, sizes= measure(dir, 0, [])
        toDelete = 0
        for size in sorted(sizes):
            if size > 30000000-(70000000-sizes[-1]):
                toDelete = size
                break
        print('Directories of size less than 100000 sum up to {0}.'.format(s))       
        print('Total disk space is 70000000, and we need 30000000 space to update.')
        print('Currently we have {0} space available, so we need {1} more'.format(70000000-sizes[-1], 30000000-(70000000-sizes[-1])))
        print('Therefore we have to delete the file with size {0}.'.format(toDelete))


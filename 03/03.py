f = open('03\input.txt', 'r')
lines = f.readlines()
priority1 = 0
priority2 = 0
for line in lines:
    line = line.strip()
    p1 = line[:int(len(line)/2)]
    p2 = line[int(len(line)/2):]
    for c in p1:
        if c in p2:
            priority1 += ord(c.swapcase())-64-int(ord(c.swapcase())/91)*6
            break    
print('Priority for part1 is {0}'.format(priority1))

for i in range(int(len(lines)/3)):
    r1 = lines[i*3]
    r2 = lines[i*3+1]
    r3 = lines[i*3+2]
    for c in r1:
        if c in r2 and c in r3:
            priority2 += ord(c.swapcase())-64-int(ord(c.swapcase())/91)*6
            break
print('Priority for part2 is {0}'.format(priority2))

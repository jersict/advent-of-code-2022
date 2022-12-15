f = open('01\input.txt', 'r')
lines = f.readlines()
total = [0]
n = 0
for line in lines:
    if line == '\n':
        total.append(0)
        n += 1
        continue
    total[n] += int(line.strip())
print('Elf that is carrying the most calories in carrying {0} calories.'.format(max(total)))
print('Top three elves are carrying {0} calories.'.format(sum(sorted(total, reverse=True)[:3])))
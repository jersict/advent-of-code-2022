f = open('02\input.txt', 'r')
lines = f.readlines()
score1 = 0
score2 = 0
for line in lines:
    line = line.strip()
    if 'X' in line:
        score1 += 1
        if 'A' in line:
            score1 += 3
            score2 += 3
        if 'B' in line:
            score2 += 1
        if 'C' in line:
            score1 += 6
            score2 += 2
    if 'Y' in line:
        score1 += 2
        score2 += 3
        if 'A' in line:
            score1 += 6
            score2 += 1
        if 'B' in line:
            score1 += 3
            score2 += 2
        if 'C' in line:
            score2 += 3
    if 'Z' in line:
        score1 += 3
        score2 += 6
        if 'A' in line:
            score2 += 2
        if 'B' in line:
            score1 += 6
            score2 += 3
        if 'C' in line:
            score1 += 3
            score2 += 1
print('Score is {0} by the first scoring and {1} by the second scoring.'.format(score1, score2))
def getTopAndBottom(trees, x, y):
    top = []
    bot = []
    for i, line in enumerate(trees):
        if i < x:
            top.append(trees[i][y])
        elif i > x:
            bot.append(trees[i][y])
    return top, bot

def measureVisible(trees):
    visible = len(trees)*2+len(trees[0])*2-4
    for x in range(1,len(trees)-1):
        for y in range(1,len(trees[0])-1):
            left = max(trees[x][:y])
            if left < trees[x][y]:
                visible += 1
                continue
            right = max(trees[x][y+1:])
            if right < trees[x][y]:
                visible += 1
                continue
            top, bottom = getTopAndBottom(trees, x, y)
            if min([max(top), max(bottom)]) < trees[x][y]:
                visible += 1
                continue
    return visible

def getVisibleTreesInLine(line, heigth):
    visible = 0
    for tree in line:
        if tree < heigth:
            visible += 1
        else:
            visible += 1
            return visible
    return visible

def getBestScenicScore(trees):
    bestScore = 0
    for x in range(1,len(trees)-1):
        for y in range(1,len(trees[0])-1):
            score = 1
            left = trees[x][:y]
            right = trees[x][y+1:]
            top, bottom = getTopAndBottom(trees, x, y)
            score *= getVisibleTreesInLine(list(reversed(left)), trees[x][y])
            score *= getVisibleTreesInLine(right, trees[x][y])
            score *= getVisibleTreesInLine(list(reversed(top)), trees[x][y])
            score *= getVisibleTreesInLine(bottom, trees[x][y])
            if score > bestScore:
                bestScore = score
    return bestScore

if __name__ == "__main__":
    with open("08/input.txt") as file:
        trees = file.readlines()
        for i, line in enumerate(trees):
            trees[i] = [*line.strip()]
        visible = measureVisible(trees)
        scenicScore = getBestScenicScore(trees)
        print('There are {0} visible trees. Best scenic score available is {1}'.format(visible, scenicScore))
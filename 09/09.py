import math
def headMovement(move, headPosition):
    match move:
        case 'R':
            headPosition[0] += 1
        case 'L':
            headPosition[0] -= 1
        case 'U':
            headPosition[1] += 1
        case 'D':
            headPosition[1] -= 1
        case _:
            exit(1)
    return headPosition

def tailMovement(headPosition, tailPosition):
    if abs(headPosition[0] - tailPosition[0]) == 2 and abs(headPosition[1] - tailPosition[1]) == 2: 
        tailPosition[0] += int((headPosition[0] - tailPosition[0])/2)
        tailPosition[1] += int((headPosition[1] - tailPosition[1])/2)
    elif abs(headPosition[0] - tailPosition[0]) == 2 :
        if headPosition[0] != tailPosition[0]:
            tailPosition[0] += math.ceil((headPosition[0] - tailPosition[0])/2)
        if headPosition[1] != tailPosition[1]:
            tailPosition[1] = headPosition[1]
    elif abs(headPosition[1] - tailPosition[1]) == 2:
        if headPosition[1] != tailPosition[1]:
            tailPosition[1] += math.ceil((headPosition[1] - tailPosition[1])/2)
        if headPosition[0] != tailPosition[0]:
            tailPosition[0] = headPosition[0]
    return tailPosition


def determineVisited(movements, length):
    rope = []
    for _ in range(length):
        rope.append([0, 0])
    visitedPositions = {}
    for move in movements:
        move = move.strip().split(' ')
        for i in range(int(move[1])):
            rope[0] = headMovement(move[0], rope[0])
            for j in range(length-1):
                rope[j+1] = tailMovement(rope[j], rope[j+1])
            if str(rope[-1]) not in list(visitedPositions.keys()):
                visitedPositions[str(rope[-1])] = 1
            else:
                visitedPositions[str(rope[-1])] += 1
    return visitedPositions


if __name__ == "__main__":
    with open("09/input.txt") as file:
        movements = file.readlines()
        visitedPositions2 = determineVisited(movements, 2)
        visitedPositions10 = determineVisited(movements, 10)
        print('Tail of rope with two knots has visited {0} positions at least once.\nTail of rope with ten knots has visited {1} positions at least once'.format(len(list(visitedPositions2.keys())), len(list(visitedPositions10.keys()))))

import numpy as np
import sys

def createMap(lines):
    miny = 200
    maxy = 0
    walls = []
    for line in lines:
        wall = []
        vertices = line.strip().split(' -> ')
        for vertex in vertices:
            coords = vertex.split(',')
            x = int(coords[0])
            y = int(coords[1])
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
            wall.append((x, y))
        walls.append(wall)
    width = 500
    height = maxy
    minx = 250
    map = np.chararray((width+3, height+3))
    map[:] = '.'
    for wall in walls:
        for i in range(len(wall)-1):
            start = wall[i]
            end = wall[i+1]
            if start[0] == end[0]:
                for j in range(min(start[1], end[1]), max(start[1], end[1])+1):
                    map[start[0]-minx][j] = '#'
            else:
                for j in range(min(start[0], end[0]), max(start[0], end[0])+1):
                    map[j-minx][start[1]] = '#'
    for m in map:
        m[-1] = '#'
    return map, minx
    
def checkIfSandOffMap(map):
    for bit in map.transpose()[-2]:
        if bit != b'.':
            return True
    return False
    
def checkIfSandOnSpawn(map, minx):
    if map[500-minx, 0] == b'o':
        return False
    return True


def moveSand(movingSand, map, stopped):
    i = 0
    while i < len(movingSand):
        sand = movingSand[i]
        if map[sand[0]][sand[1]+1] == b'.':
            map[sand[0]][sand[1]+1] = 'o'
            map[sand[0]][sand[1]] = '.'
            movingSand[i] = [movingSand[i][0], movingSand[i][1]+1]
            i += 1
        elif map[sand[0]-1][sand[1]+1] == b'.':
            map[sand[0]-1][sand[1]+1] = 'o'
            map[sand[0]][sand[1]] = '.'
            movingSand[i] = [movingSand[i][0]-1, movingSand[i][1]+1]
            i += 1
        elif map[sand[0]+1][sand[1]+1] == b'.':
            map[sand[0]+1][sand[1]+1] = 'o'
            map[sand[0]][sand[1]] = '.'
            movingSand[i] = [movingSand[i][0]+1, movingSand[i][1]+1]
            i += 1
        elif sand[1] == 0:
            print('Sand has stopped coming after {0} grains.'.format(stopped+1))
            exit()
        else:
            stopped += 1
            movingSand.pop(0)
    return movingSand, map, stopped

def fillWithSand(map, minx):
    movingSand = []
    p1 = True
    stopped = 0
    while checkIfSandOnSpawn(map, minx):
        movingSand.append([500-minx, 0])
        movingSand, map, stopped = moveSand(movingSand, map, stopped)
        if p1 and checkIfSandOffMap(map):
            print('{0} grains of sand have stopped before the first trickled beyond the lowest line.'.format(stopped))
            p1 = False

if __name__ == "__main__":
    with open("14/input.txt") as file:
        lines = file.readlines()
        map, minx = createMap(lines)
        fillWithSand(map, minx)
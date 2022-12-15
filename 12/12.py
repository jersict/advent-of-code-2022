import math
import copy

def dijkstra(distances, map, start, end):
    x = start[0]
    y = start[1]
    distances[start] = 0
    done = {}
    final_distances = {}
    while x != end[0] or y != end[1]:
        if 0 <= x-1 and (x-1, y) not in done.keys():
            if map[x-1][y] - map[x][y] <= 1:
                distances[(x-1, y)] =  min(distances[(x, y)] + 1, distances[(x-1, y)])
            else:
                distances[(x-1, y)] =  min(distances[(x, y)] + 10000, distances[(x-1, y)])
        if x+1 < len(map) and (x+1, y) not in done.keys():
            if map[x+1][y] - map[x][y] <= 1:
                distances[(x+1, y)] =  min(distances[(x, y)] + 1, distances[(x+1, y)])
            else:
                distances[(x+1, y)] =  min(distances[(x, y)] + 10000, distances[(x+1, y)])
        if 0 <= y-1 and (x, y-1) not in done.keys():
            if map[x][y-1] - map[x][y] <= 1:
                distances[(x, y-1)] =  min(distances[(x, y)] + 1, distances[(x, y-1)])
            else:
                distances[(x, y-1)] =  min(distances[(x, y)] + 10000, distances[(x, y-1)])
        if y+1 < len(map[0]) and (x, y+1) not in done.keys():
            if map[x][y+1] - map[x][y] <= 1:
                distances[(x, y+1)] =  min(distances[(x, y)] + 1, distances[(x, y+1)])
            else:
                distances[(x, y+1)] =  min(distances[(x, y)] + 10000, distances[(x, y+1)])
        done[(x, y)] = distances.pop((x, y))
        shortest = min(distances, key=distances.get)
        x = shortest[0]
        y = shortest[1]
    return distances
        

def createMap(lines):
    map = []
    distances = {}
    starts = []
    for i, line in enumerate(lines):
        if 'S' in line:
            start = (i, line.index('S'))
        if 'E' in line:
            end = (i, line.index('E'))
        l = []
        for j, c in enumerate(line.strip()):
            pos = (i, j)
            if c == 'a': 
                starts.append(pos)
            distances[pos] = math.inf
            l.append(ord(c)-96)
        map.append(l)
    map[start[0]][start[1]] = 1
    map[end[0]][end[1]] = 26
    

    return map, start, end, distances, starts


if __name__ == "__main__":
    with open("12/input.txt") as file:
        lines = file.readlines()
        map, start, end, distances, starts = createMap(lines)
        finish = dijkstra(copy.deepcopy(distances), map, start, end)
        best = finish[end]
        print('Fewest amount of steps required for first trail is {0}.'.format(best))
        for s in starts:
            finish = dijkstra(copy.deepcopy(distances), map, s, end)
            if finish[end] < best:
                best = finish[end]
        print('Best trail is {0} steps long.'.format(best))
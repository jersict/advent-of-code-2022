from sympy import Interval, Union, Intersection

def union(intervals):
    """ Union of a list of intervals e.g. [(1,2),(3,4)] """
    u = Union(*intervals)
    return [list(u.args[:2])] if isinstance(u, Interval) \
       else list(u.args)

def unionWithinArea(intervals, area):
    """ Union of a list of intervals e.g. [(1,2),(3,4)] """
    u = Intersection(Union(*intervals), area)
    return [list(u.args[:2])] if isinstance(u, Interval) \
       else list(u.args)

class Sensor:
    def __init__(self, x, y, beaconX, beaconY, distance):
        self.x = x
        self.y = y
        self.beaconX = beaconX
        self.beaconY = beaconY
        self.distance = distance

    def coverageOfRow(self, row):
        span = self.distance - abs(self.y - row)
        if span < 1:
            return 0
        else:
            return Interval(self.x - span, self.x + span)


def getSensor(line):
    line = line.replace('Sensor at ', '').replace('x=', '').replace('y=', '').replace('closest beacon is at ', '')
    beacon = line.split(': ')[1].split(', ')
    sensor = line.split(': ')[0].split(', ')
    sx = int(sensor[0])
    sy = int(sensor[1])
    bx = int(beacon[0])
    by = int(beacon[1])
    dist = abs(sx-bx) + abs(sy-by)
    return Sensor(sx, sy, bx, by, dist)

if __name__ == "__main__":
    with open("15/input.txt") as file:
        lines = file.readlines()
        edge = 4000000
        scannedLine = 2000000
        coverage = []
        sensors = []
        noBeacon = 0
        for line in lines:
            sensor = getSensor(line)
            sensors.append(sensor)
            coverageOfRow = sensor.coverageOfRow(scannedLine)
            if coverageOfRow != 0:
                coverage.append(coverageOfRow)
        coverage = union(coverage)
        for cover in coverage:
            noBeacon += abs(cover[1]-cover[0])
        print('Total coverage of line {0} is {1}.'.format(scannedLine, noBeacon))
        for i in range(edge):
            coverage = []
            for sensor in sensors:
                coverageOfRow = sensor.coverageOfRow(i)
                if coverageOfRow != 0:
                    coverage.append(coverageOfRow)
            coverage = unionWithinArea(coverage, Interval(0, edge))
            if len(coverage) > 1:
                print('Frequency is {0}.'.format((coverage[0].end+1)*4000000 + i))
                exit(0)


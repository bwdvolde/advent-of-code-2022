import re
from dataclasses import dataclass

from read_file.read_file import read_file

lines = read_file("input.txt")


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Sensor:
    location: Point
    closest_beacon: Point

    def distance_to_closest_beacon(self):
        return abs(self.location.x - self.closest_beacon.x) + abs(self.location.y - self.closest_beacon.y)


sensors = []
for line in lines:
    starting_items = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line).groups()
    location = Point(int(starting_items[0]), int(starting_items[1]))
    closest_beacon = Point(int(starting_items[2]), int(starting_items[3]))
    sensor = Sensor(location, closest_beacon)
    sensors.append(sensor)

LIMIT = 4_000_000


def calculate_distres_beacon_position(y) -> Point | None:
    intervals = []
    for sensor in sensors:
        left = sensor.location.x - sensor.distance_to_closest_beacon() + abs(sensor.location.y - y)
        left = max(0, left)
        right = sensor.location.x + sensor.distance_to_closest_beacon() - abs(sensor.location.y - y)
        right = min(right, LIMIT)
        # print(sensor, left, right, set(range(left, right + 1)))

        if left < right:
            intervals.append((left, right))

    intervals.sort(key=lambda x: x[0])

    current_max = intervals[0][1]
    for interval in intervals:
        if current_max + 2 == interval[0]:
            print(intervals, current_max, interval)
            return Point(current_max + 1, y)
        current_max = max(current_max, interval[1])
    return None


for y in range(3_000_000, LIMIT + 1):
    if y % 100_000 == 0:
        print(y)
    result = calculate_distres_beacon_position(y)
    if result:
        print(result.x * 4_000_000 + result.y)
        print(result)

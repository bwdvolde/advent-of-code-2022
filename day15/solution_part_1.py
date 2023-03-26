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

desired_y = 2_000_000

forbidden = set()
for sensor in sensors:
    left = sensor.location.x - sensor.distance_to_closest_beacon() + abs(sensor.location.y - desired_y)
    right = sensor.location.x + sensor.distance_to_closest_beacon() - abs(sensor.location.y - desired_y)
    # print(sensor, left, right, set(range(left, right + 1)))
    forbidden |= set(range(left, right + 1))

taken_by_sensor_at_desired_y = set(sensor.closest_beacon.x for sensor in sensors if sensor.closest_beacon.y == desired_y)
forbidden -= taken_by_sensor_at_desired_y
print(forbidden)


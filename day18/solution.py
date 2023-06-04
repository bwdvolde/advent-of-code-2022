from dataclasses import dataclass
from queue import Queue
from typing import List, Set

from read_file.read_file import read_file


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int


def parse():
    lines = read_file("input.txt")
    points = []
    for line in lines:
        points.append(Point(*map(int, line.split(","))))

    return points


def neighbours(point: Point) -> Set[Point]:
    return {
        Point(point.x + 1, point.y, point.z),
        Point(point.x - 1, point.y, point.z),
        Point(point.x, point.y + 1, point.z),
        Point(point.x, point.y - 1, point.z),
        Point(point.x, point.y, point.z + 1),
        Point(point.x, point.y, point.z - 1),
    }


points = set(parse())

surface_area_part_1 = 0
for point in points:
    surface_area_part_1 += sum(1 for neighbour in neighbours(point) if neighbour not in points)
print(f"Part 1: {surface_area_part_1}")

potential_surface_points = {neighbour for point in points for neighbour in neighbours(point) if neighbour not in points}

min_x = min(point.x for point in potential_surface_points)
max_x = max(point.x for point in potential_surface_points)
min_y = min(point.y for point in potential_surface_points)
max_y = max(point.y for point in potential_surface_points)
min_z = min(point.z for point in potential_surface_points)
max_z = max(point.z for point in potential_surface_points)


def in_bounds(point: Point) -> bool:
    return min_x <= point.x <= max_x and min_y <= point.y <= max_y and min_z <= point.z <= max_z


certainly_a_surface_point = [point for point in potential_surface_points if point.x == min_x][0]

surface_points = {certainly_a_surface_point}
visited = set()
queue = Queue()
queue.put(certainly_a_surface_point)
while not queue.empty():
    current = queue.get()
    for neighbour in neighbours(current):
        if neighbour not in visited and in_bounds(neighbour) and neighbour not in points:
            queue.put(neighbour)
            visited.add(neighbour)
            if neighbour in potential_surface_points:
                surface_points.add(neighbour)

surface_area_part_2 = 0
for point in points:
    surface_area_part_2 += sum(1 for neighbour in neighbours(point) if neighbour in surface_points)
print(f"Part 2: {surface_area_part_2}")

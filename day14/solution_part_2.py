from dataclasses import dataclass

from read_file.read_file import read_file

lines = read_file("input.txt")


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


rocks = set()
for line in lines:
    unparsed_break_points = line.split(" -> ")
    break_points = [Point(*map(int, unparsed_break_point.split(","))) for unparsed_break_point in unparsed_break_points]
    for (start, end) in zip(break_points, break_points[1:]):
        dx = (start.x < end.x) - (start.x > end.x)
        dy = (start.y < end.y) - (start.y > end.y)
        current = start
        while current != end:
            rocks.add(current)
            current += Point(dx, dy)
        rocks.add(current)
max_y = max(rock.y for rock in rocks)
rocks |= {Point(x, max_y + 2) for x in range(-100_000, 100_000)}
occupied = set(rocks)

amount_that_can_rest = 0
while True:
    current = Point(500, 0)
    can_move = True
    while can_move:
        can_move = False
        possible_directions = [Point(0, 1), Point(-1, 1), Point(1, 1)]
        for possible_direction in possible_directions:
            if current + possible_direction not in occupied:
                current += possible_direction
                can_move = True
                break

    occupied.add(current)
    amount_that_can_rest += 1

    if current == Point(500, 0):
        break

print(f"Part 2: {amount_that_can_rest}")

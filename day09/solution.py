import math
from dataclasses import dataclass

from read_file.read_file import read_file


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Motion:
    direction: str
    amount: int


UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

DIRECTION_TO_DIFF = {
    UP: Point(0, -1),
    DOWN: Point(0, 1),
    LEFT: Point(-1, 0),
    RIGHT: Point(1, 0),
}
lines = read_file("input.txt")


def dist(a: Point, b: Point) -> int:
    return int(math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2)))


motions = []
for line in lines:
    direction, amount = line.split(" ")
    motions.append(Motion(direction, int(amount)))


def calculate_unique_places(rope_length):
    rope = [Point(0, 0)] * rope_length
    visited = {rope[-1]}
    for motion in motions:
        for _ in range(motion.amount):
            diff = DIRECTION_TO_DIFF[motion.direction]
            rope[0] = rope[0] + diff
            for i in range(1, len(rope)):
                if dist(rope[i - 1], rope[i]) > 1:
                    dx = 0
                    if rope[i - 1].x < rope[i].x:
                        dx = -1
                    elif rope[i - 1].x > rope[i].x:
                        dx = 1

                    dy = 0
                    if rope[i - 1].y < rope[i].y:
                        dy = -1
                    elif rope[i - 1].y > rope[i].y:
                        dy = 1
                    rope[i] = rope[i] + Point(dx, dy)
            visited.add(rope[-1])
    return len(visited)


def print_rope(rope):
    for y in range(-20, 20):
        for x in range(-20, 20):
            point = Point(x, y)
            if point in rope:
                print(rope.index(point), end="")
            else:
                print(".", end="")
        print()
    print()


print(f"Part 1: {calculate_unique_places(rope_length=2)}")
print(f"Part 2: {calculate_unique_places(rope_length=10)}")

import math
from dataclasses import dataclass
from functools import lru_cache
from queue import Queue

from read_file.read_file import read_file


@dataclass(frozen=True, eq=True)
class Position:
    row: int
    col: int

    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.col)


@dataclass
class Blizzard:
    position: Position
    direction: Position


NORTH = Position(-1, 0)
SOUTH = Position(1, 0)
WEST = Position(0, -1)
EAST = Position(0, 1)
STAND_STILL = Position(0, 0)

ALL_DIRECTIONS = [SOUTH, EAST, NORTH, WEST, STAND_STILL]


def manhattan_distance(a: Position, b: Position) -> int:
    return abs(a.row - b.row) + abs(a.col - b.col)


lines = read_file("input.txt")

initial_blizzards = []
for r, line in enumerate(lines[1:-1]):
    for c, char in enumerate(line[1:-1]):
        position = Position(r, c)
        match char:
            case "^":
                initial_blizzards.append(Blizzard(position, NORTH))
            case "v":
                initial_blizzards.append(Blizzard(position, SOUTH))
            case "<":
                initial_blizzards.append(Blizzard(position, WEST))
            case ">":
                initial_blizzards.append(Blizzard(position, EAST))

height = len(lines) - 2
width = len(lines[0]) - 2

start_position = Position(-1, 0)
end_position = Position(height, width - 1)

upper_bound = 1000


@lru_cache(maxsize=None)
def calculate_blizzard_list(time):
    if time == 0:
        return initial_blizzards
    previous_blizzards = calculate_blizzard_list(time - 1)
    blizzards = []
    for previous_blizzard in previous_blizzards:
        blizzard = Blizzard(previous_blizzard.position, previous_blizzard.direction)
        new_row = (blizzard.position.row + blizzard.direction.row) % height
        new_col = (blizzard.position.col + blizzard.direction.col) % width
        blizzard.position = Position(new_row, new_col)
        blizzards.append(blizzard)
    return blizzards


@lru_cache(maxsize=None)
def calculate_occupied_positions(time):
    return {blizzard.position for blizzard in calculate_blizzard_list(time)}


FAKE_NONE_VALUE = "none"

FIRST_TO_END_DESTINATION = 0
TO_START_DESTINATION = 1
SECOND_TO_END_DESTINATION = 2


def calculate_shortest_length():
    queue = Queue()

    mod_to_use = math.lcm(width, height)

    queue.put((0, start_position, FIRST_TO_END_DESTINATION))
    visited = {0, start_position, FIRST_TO_END_DESTINATION}
    while True:
        time, position, part = queue.get()
        if position == end_position and part == SECOND_TO_END_DESTINATION:
            return time

        new_part = part
        if part == FIRST_TO_END_DESTINATION and position == end_position:
            new_part = TO_START_DESTINATION
        elif part == TO_START_DESTINATION and position == start_position:
            new_part = SECOND_TO_END_DESTINATION

        for direction in ALL_DIRECTIONS:
            new_position = position + direction
            new_time = time + 1
            occupied_positions = calculate_occupied_positions(new_time % mod_to_use)
            key = (new_time % mod_to_use, new_position, new_part)
            is_valid_position = new_position in [start_position, end_position] or (
                    0 <= new_position.row < height and 0 <= new_position.col < width)
            if is_valid_position and new_position not in occupied_positions and key not in visited:
                visited.add(key)
                queue.put((new_time, new_position, new_part))


print(f"Part 2: {calculate_shortest_length()}")

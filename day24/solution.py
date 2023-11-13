import math
from copy import deepcopy
from dataclasses import dataclass
from functools import lru_cache

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


def calculate_shortest_length():
    cache = {}

    upper_bound = 1000

    def recurse(position, current_time):
        nonlocal upper_bound
        if current_time >= upper_bound:
            return FAKE_NONE_VALUE
        current_time_mod = current_time
        cache_key = (position, current_time_mod)
        if cache_key in cache:
            return cache[cache_key]

        if position == end_position:
            upper_bound = min(upper_bound, current_time)
            print(upper_bound)
            return 0

        result = FAKE_NONE_VALUE

        occupied_positions = calculate_occupied_positions(current_time_mod)
        is_valid_position = position == start_position or (
                0 <= position.row < height and 0 <= position.col < width and position not in occupied_positions)
        if is_valid_position:
            possible_shortest_lengths = []
            for direction in ALL_DIRECTIONS:
                recursive_result = recurse(position + direction, current_time + 1)
                if recursive_result is not FAKE_NONE_VALUE:
                    possible_shortest_lengths.append(recursive_result)

            if possible_shortest_lengths:
                result = min(possible_shortest_lengths) + 1

        cache[cache_key] = result
        return result

    return recurse(start_position, 0)


print(f"Part 1: {calculate_shortest_length()}")

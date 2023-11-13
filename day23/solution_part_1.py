from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from typing import List, Set, Optional

from read_file.read_file import read_file


@dataclass(frozen=True, eq=True)
class Position:
    row: int
    col: int

    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.col)


NORTH = Position(-1, 0)
NORTH_EAST = Position(-1, 1)
NORTH_WEST = Position(-1, -1)
SOUTH = Position(1, 0)
SOUTH_EAST = Position(1, 1)
SOUTH_WEST = Position(1, -1)
WEST = Position(0, -1)
EAST = Position(0, 1)

ALL_DIRECTIONS = [
    NORTH,
    NORTH_EAST,
    NORTH_WEST,
    SOUTH,
    SOUTH_EAST,
    SOUTH_WEST,
    WEST,
    EAST,
]

ADJACENT_POSITION_LIST = [
    [NORTH_WEST, NORTH, NORTH_EAST],
    [SOUTH_WEST, SOUTH, SOUTH_EAST],
    [NORTH_WEST, WEST, SOUTH_WEST],
    [NORTH_EAST, EAST, SOUTH_EAST],
]

lines = read_file("input.txt")


def print_positions(positions: Set[Position]):
    min_row = min(position.row for position in positions)
    max_row = max(position.row for position in positions)
    min_col = min(position.col for position in positions)
    max_col = max(position.col for position in positions)

    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if Position(row, col) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")


def calculate_empty_ground_tiles(positions: Set[Position]):
    min_row = min(position.row for position in positions)
    max_row = max(position.row for position in positions)
    min_col = min(position.col for position in positions)
    max_col = max(position.col for position in positions)

    n_empty_ground_tiles = 0
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if Position(row, col) not in positions:
                n_empty_ground_tiles += 1

    return n_empty_ground_tiles


current_positions = set()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            current_positions.add(Position(r, c))

n_rounds = 10


def calculate_next_position(position: Position, round_offset) -> Optional[Position]:
    has_neighbours = any(position + direction in current_positions for direction in ALL_DIRECTIONS)
    if has_neighbours:
        i = 0
        while i < 4:
            adjacent_positions = ADJACENT_POSITION_LIST[(round_offset + i) % len(ADJACENT_POSITION_LIST)]
            if all(position + adjacent_position not in current_positions for adjacent_position in
                   adjacent_positions):
                return position + adjacent_positions[1]
            i += 1
    return None


for round in range(n_rounds):
    round_offset = round % len(ADJACENT_POSITION_LIST)

    unfiltered_next_positions = []

    current_to_next_position = {current_position: calculate_next_position(current_position, round_offset) for current_position in current_positions}
    valid_next_positions = {position for position, count in Counter(current_to_next_position.values()).items() if count == 1}
    next_positions = set()
    for current_position in current_positions:
        next_position = current_to_next_position[current_position]
        if next_position in valid_next_positions:
            next_positions.add(next_position)
        else:
            next_positions.add(current_position)

    current_positions = next_positions

print(f"Part 1: {calculate_empty_ground_tiles(current_positions)}")

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Optional

import numpy as np

from read_file.read_file import read_file

EXAMPLE = "example.txt"
INPUT = "input.txt"
FILE = INPUT


@dataclass
class Node:
    original_row: int
    original_col: int
    char: str

    grid: Optional[int]
    left: Optional[Node]
    right: Optional[Node]
    top: Optional[Node]
    down: Optional[Node]

    def __repr__(self):
        return f"{self.grid}: ({self.original_row, self.original_col})"


@dataclass(frozen=True)
class Position:
    row: int
    char: int

    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.char)


UP = Position(-1, 0)
DOWN = Position(1, 0)
LEFT = Position(0, -1)
RIGHT = Position(0, 1)

ROTATE_LEFT = {
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
    RIGHT: UP,
}

ROTATE_RIGHT = {v: k for k, v in ROTATE_LEFT.items()}


def parse_raw():
    lines = read_file(FILE)

    raw_grid = []
    iterator = iter(lines)
    while line := next(iterator):
        raw_grid.append(line)

    width = max(len(row) for row in raw_grid)

    # Because rows of grid do not a have trailing white spaces
    raw_grid = [row.ljust(width) for row in raw_grid]

    raw_path = next(iterator)

    raw_instructions = re.findall("[0-9]+|[RL]", raw_path)

    instructions = []
    for raw_instruction in raw_instructions:
        if raw_instruction not in ["L", "R"]:
            instructions.append(int(raw_instruction))
        else:
            instructions.append(raw_instruction)

    return raw_grid, instructions


raw_grid, instructions = parse_raw()
width = max(len(row) for row in raw_grid)
height = len(raw_grid)

grid = []
for r, row in enumerate(raw_grid):
    grid.append([])
    for c, char in enumerate(row):
        if char != " ":
            grid[-1].append(Node(r, c, char, None, None, None, None, None))
        else:
            grid[-1].append(None)
        pass
grid = np.array(grid)
grid_size = math.gcd(width, height)


def get_subgrid(row, col):
    return grid[row * grid_size:(row + 1) * grid_size, col * grid_size:(col + 1) * grid_size]


# Example sub grids
# ------
# |  1 |
# |234 |
# |  56|
# ------

# Desired sub grid structure
# ------
# | 1 |
# | 2 |
# |536|
# | 4 |
# ------
if FILE == EXAMPLE:
    grid_1 = np.rot90(get_subgrid(1, 0), -1)
    grid_2 = np.rot90(get_subgrid(1, 1), -1)
    grid_3 = np.rot90(get_subgrid(1, 2), -1)
    grid_4 = get_subgrid(2, 3)
    grid_5 = np.rot90(get_subgrid(2, 2), -1)
    grid_6 = np.rot90(get_subgrid(0, 2), -1)
else:
    grid_1 = get_subgrid(0, 1)
    grid_2 = get_subgrid(1, 1)
    grid_3 = get_subgrid(2, 1)
    grid_4 = np.rot90(get_subgrid(3, 0))
    grid_5 = get_subgrid(2, 0)
    grid_6 = np.rot90(np.rot90(get_subgrid(0, 2)))
    pass

grids = [grid_1, grid_2, grid_3, grid_4, grid_5, grid_6]

for grid_id_minus_1, current_grid in enumerate(grids):
    for r, row in enumerate(current_grid):
        for c, node in enumerate(row):
            node.grid = grid_id_minus_1 + 1
            if r > 0:
                node.top = current_grid[r - 1, c]
            if r < grid_size - 1:
                node.down = current_grid[r + 1, c]
            if c > 0:
                node.left = current_grid[r, c - 1]
            if c < grid_size - 1:
                node.right = current_grid[r, c + 1]

for c, node in enumerate(grid_1[0, :]):
    node.top = grid_4[-1, c]
for c, node in enumerate(grid_1[-1, :]):
    node.down = grid_2[0, c]
for r, node in enumerate(grid_1[:, 0]):
    node.left = np.flip(grid_5[:, 0])[r]
for r, node in enumerate(grid_1[:, -1]):
    node.right = np.flip(grid_6[:, -1])[r]

for c, node in enumerate(grid_2[0, :]):
    node.top = grid_1[-1, c]
for c, node in enumerate(grid_2[-1, :]):
    node.down = grid_3[0, c]
for r, node in enumerate(grid_2[:, 0]):
    node.left = grid_5[0, r]
for r, node in enumerate(grid_2[:, -1]):
    node.right = np.flip(grid_6[0, :])[r]

for c, node in enumerate(grid_3[0, :]):
    node.top = grid_2[-1, c]
for c, node in enumerate(grid_3[-1, :]):
    node.down = grid_4[0, c]
for r, node in enumerate(grid_3[:, 0]):
    node.left = grid_5[r, -1]
for r, node in enumerate(grid_3[:, -1]):
    node.right = grid_6[r, 0]

for c, node in enumerate(grid_4[0, :]):
    node.top = grid_3[-1, c]
for c, node in enumerate(grid_4[-1, :]):
    node.down = grid_1[0, c]
for r, node in enumerate(grid_4[:, 0]):
    node.left = np.flip(grid_5[-1, :])[r]
for r, node in enumerate(grid_4[:, -1]):
    node.right = grid_6[-1, r]

for c, node in enumerate(grid_5[0, :]):
    node.top = grid_2[c, 0]
for c, node in enumerate(grid_5[-1, :]):
    node.down = np.flip(grid_4[:, 0])[c]
for r, node in enumerate(grid_5[:, 0]):
    node.left = np.flip(grid_1[:, 0])[r]
for r, node in enumerate(grid_5[:, -1]):
    node.right = grid_3[r, 0]

for c, node in enumerate(grid_6[0, :]):
    node.top = np.flip(grid_2[:, -1])[c]
for c, node in enumerate(grid_6[-1, :]):
    node.down = grid_4[c, -1]
for r, node in enumerate(grid_6[:, 0]):
    node.left = grid_3[r, -1]
for r, node in enumerate(grid_6[:, -1]):
    node.right = np.flip(grid_1[:, -1])[r]

nodes = [node for _grid in grids for node in _grid.flatten()]
first_row_nodes = [node for node in nodes if node.original_row == 0]
current_node = min(first_row_nodes, key=lambda node: node.original_col)
# We do a rotation on the example so we start with going down instead
current_direction = DOWN if FILE == EXAMPLE else RIGHT

for node in nodes:
    if node.down is None:
        print(node)

taken_path = [Position(current_node.original_row, current_node.original_col)]


def print_grid():
    nodes_map = {Position(node.original_row, node.original_col): node for node in nodes}
    taken_path_set = set(taken_path)
    for r, row in enumerate(raw_grid):
        for c, _ in enumerate(row):
            matching_node = nodes_map.get(Position(r, c))
            if matching_node:
                if Position(matching_node.original_row, matching_node.original_col) in taken_path_set:
                    print("X", end="")
                else:
                    print(matching_node.char, end="")
            else:
                print(" ", end="")
        print()


for instruction_index, instruction in enumerate(instructions):
    if instruction == "L":
        current_direction = ROTATE_LEFT[current_direction]
    elif instruction == "R":
        current_direction = ROTATE_RIGHT[current_direction]
    else:
        remaining_steps = instruction

        while remaining_steps:
            if current_direction == UP:
                next_node = current_node.top
            if current_direction == DOWN:
                next_node = current_node.down
            if current_direction == LEFT:
                next_node = current_node.left
            if current_direction == RIGHT:
                next_node = current_node.right
            if next_node.char == "#":
                break

            if current_node.grid == 1:
                if next_node.grid == 5:
                    current_direction = RIGHT
                if next_node.grid == 6:
                    current_direction = LEFT
            elif current_node.grid == 2:
                if next_node.grid == 5:
                    current_direction = DOWN
                if next_node.grid == 6:
                    current_direction = DOWN
            elif current_node.grid == 4:
                if next_node.grid == 5:
                    current_direction = UP
                if next_node.grid == 6:
                    current_direction = UP
            elif current_node.grid == 5:
                if next_node.grid == 1:
                    current_direction = RIGHT
                if next_node.grid == 2:
                    current_direction = RIGHT
                if next_node.grid == 4:
                    current_direction = RIGHT
            elif current_node.grid == 6:
                if next_node.grid == 1:
                    current_direction = LEFT
                if next_node.grid == 2:
                    current_direction = LEFT
                if next_node.grid == 4:
                    current_direction = LEFT
            current_node = next_node
            taken_path.append(Position(current_node.original_row, current_node.original_col))
            remaining_steps -= 1

# We end up in square 6 and go right. Square 6 has been rotated 180 degrees so actually go left
score_direction = 2
part_2 = 1000 * (current_node.original_row + 1) + 4 * (current_node.original_col + 1) + score_direction
print(f"Part 2: {part_2}")

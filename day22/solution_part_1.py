import re
from dataclasses import dataclass

from read_file.read_file import read_file


@dataclass(frozen=True)
class Position:
    row: int
    col: int

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


def parse():
    lines = read_file("input.txt")

    grid = []
    iterator = iter(lines)
    while line := next(iterator):
        grid.append(line)

    width = max(len(row) for row in grid)

    # Because rows of grid do not a have trailing white spaces
    grid = [row.ljust(width) for row in grid]

    raw_path = next(iterator)

    raw_instructions = re.findall("[0-9]+|[RL]", raw_path)

    instructions = []
    for raw_instruction in raw_instructions:
        if raw_instruction not in ["L", "R"]:
            instructions.append(int(raw_instruction))
        else:
            instructions.append(raw_instruction)

    return grid, instructions


grid, instructions = parse()
width = max(len(row) for row in grid)

# Not universally applicable but works on my input
current_direction = RIGHT
current_position = Position(0, grid[0].index("."))

for instruction in instructions:
    if instruction == "L":
        current_direction = ROTATE_LEFT[current_direction]
    elif instruction == "R":
        current_direction = ROTATE_RIGHT[current_direction]
    else:
        remaining_steps = instruction
        while remaining_steps:

            next_position = current_position
            while True:
                next_position = (next_position + current_direction)
                next_position = Position(next_position.row % len(grid), next_position.col % width)
                if grid[next_position.row][next_position.col] != " ":
                    break
            next_tile = grid[next_position.row][next_position.col]
            if next_tile == "#":
                remaining_steps = 0
            elif next_tile == ".":
                remaining_steps -= 1
                current_position = next_position

if current_direction == RIGHT:
    score_direction = 0
elif current_direction == DOWN:
    score_direction = 1
elif current_direction == LEFT:
    score_direction = 2
elif current_direction == RIGHT:
    score_direction = 3

part_1 = 1000 * (current_position.row + 1) + 4 * (current_position.col + 1) + score_direction
print(f"Part 1: {part_1}")

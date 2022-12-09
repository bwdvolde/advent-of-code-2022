import re
from dataclasses import dataclass

from read_file.read_file import read_file

lines = read_file("input.txt")

parsing_stacks = True
n_stacks = None
rows = []

iterator = iter(lines)
while parsing_stacks:
    line = next(iterator)
    row = line[1::4]
    parsing_stacks = row[0] != "1"
    if parsing_stacks:
        rows.append(row)
    else:
        n_stacks = len(row)

rows = [f"{{:<{n_stacks}}}".format(row) for row in rows]
stacks = [[] for _ in range(n_stacks)]

for row in reversed(rows):
    for i, element in enumerate(row):
        if element != " ":
            stacks[i].append(element)

next(iterator)


@dataclass
class Move:
    amount: int
    from_stack: int
    to_stack: int


moves = []
while True:
    try:
        line = next(iterator)
        amount, from_stack, to_stack = re.match("move (.+) from (.+) to (.+)", line).groups()
        moves.append(Move(int(amount), int(from_stack) - 1, int(to_stack) - 1))
    except StopIteration:
        break

for move in moves:
    for _ in range(move.amount):
        element = stacks[move.from_stack].pop()
        stacks[move.to_stack].append(element)

part_1 = "".join([stack[-1] for stack in stacks])
print(f"Part 1: {part_1}")

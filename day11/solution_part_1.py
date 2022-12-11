import re
from dataclasses import dataclass
from typing import List

from read_file.read_file import read_file


@dataclass
class Monkey:
    items: List[int]
    operation_operator: str
    operation_left: str
    operation_right: str
    test_param: int
    throw_to_if_true: int
    throw_to_if_false: int

    n_inspections: int


lines = read_file("input.txt")
iterator = iter(lines)
monkeys = []
while True:
    try:
        # Read Monkey x
        next(iterator)

        starting_items_raw = next(iterator)
        starting_items = re.match(".*Starting items: (.*)", starting_items_raw).groups()[0]
        starting_items = starting_items.split(", ")
        starting_items = list(map(int, starting_items))

        operation_left, operation_operator, operation_right = re.match(".*Operation: new = (.*) (.) (.*)",
                                                                       next(iterator)).groups()

        divisible = int(re.match(".*Test: divisible by (.*)", next(iterator)).group(1))
        throw_to_if_true = int(re.match(".*If true: throw to monkey (.*)", next(iterator)).group(1))
        throw_to_if_false = int(re.match(".*If false: throw to monkey (.*)", next(iterator)).group(1))

        monkey = Monkey(starting_items, operation_operator, operation_left, operation_right, divisible,
                        throw_to_if_true, throw_to_if_false, 0)
        monkeys.append(monkey)

        next(iterator)
    except StopIteration:
        break

for _ in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            left = int(monkey.operation_left) if monkey.operation_left.isdigit() else item
            right = int(monkey.operation_right) if monkey.operation_right.isdigit() else item
            new_item = left + right if monkey.operation_operator == "+" else left * right
            new_item = new_item // 3

            if not new_item % monkey.test_param:
                monkeys[monkey.throw_to_if_true].items.append(new_item)
            else:
                monkeys[monkey.throw_to_if_false].items.append(new_item)
        monkey.n_inspections += len(monkey.items)
        monkey.items = []

n_inspections_list = [monkey.n_inspections for monkey in monkeys]
n_inspections_list.sort(reverse=True)
print(f"Part 1: {n_inspections_list[0] * n_inspections_list[1]}")

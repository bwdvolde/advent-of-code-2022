import re
from abc import abstractmethod
from dataclasses import dataclass

from read_file.read_file import read_file

HUMAN = "humn"


class Monkey:

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def contains(self, monkey_name):
        pass

    @abstractmethod
    def find_human(self, required_total):
        pass


@dataclass
class NumberMonkey(Monkey):
    name: str
    number: int

    def eval(self):
        return self.number

    def contains(self, monkey_name):
        return self.name == monkey_name

    def find_human(self, required_total):
        if self.name == HUMAN:
            return required_total
        raise Exception("This should not happen")


@dataclass
class OperationMonkey(Monkey):
    name: str
    operation: str
    left: Monkey
    right: Monkey

    def eval(self):
        match self.operation:
            case "+":
                return self.left.eval() + self.right.eval()
            case "-":
                return self.left.eval() - self.right.eval()
            case "*":
                return self.left.eval() * self.right.eval()
            case "/":
                return self.left.eval() // self.right.eval()

    def contains(self, monkey_name):
        return self.left.contains(monkey_name) or self.right.contains(monkey_name)

    def find_human(self, required_total):
        human_in_left = self.left.contains(HUMAN)
        if human_in_left:
            # No unknown parameter in right so we can evaluate it
            right_eval = self.right.eval()
            match self.operation:
                case "+":
                    return self.left.find_human(required_total - right_eval)
                case "-":
                    return self.left.find_human(required_total + right_eval)
                case "*":
                    return self.left.find_human(required_total // right_eval)
                case "/":
                    return self.left.find_human(required_total * right_eval)
        else:
            left_eval = self.left.eval()
            match self.operation:
                case "+":
                    return self.right.find_human(required_total - left_eval)
                case "-":
                    return self.right.find_human(left_eval - required_total)
                case "*":
                    return self.right.find_human(required_total // left_eval)
                case "/":
                    return self.right.find_human(left_eval // required_total)


name_to_monkey = {}

lines = read_file("input.txt")
for line in lines:
    number_match = re.match("^([a-z]+): ([0-9]+)$", line)
    if number_match:
        name, number = number_match.groups()
        number = int(number)
        name_to_monkey[name] = NumberMonkey(name, number)
    else:
        operation_match = re.match("^([a-z]+): ([a-z]+) (\\+|-|\\*|/) ([a-z]+)$", line)
        name, left, operation, right = operation_match.groups()
        name_to_monkey[name] = OperationMonkey(name, operation, NumberMonkey(left, 0), NumberMonkey(right, 0))

for monkey in name_to_monkey.values():
    if isinstance(monkey, OperationMonkey):
        monkey.left = name_to_monkey[monkey.left.name]
        monkey.right = name_to_monkey[monkey.right.name]

root = name_to_monkey["root"]
human = name_to_monkey[HUMAN]
part_1 = root.eval()
print(f"Part 1: {part_1}")

# Left and right have to be equal this is the same as saying left - right = 0
root.operation = "-"
part_2 = root.find_human(0)
print(f"Part 2: {part_2}")

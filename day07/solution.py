import re
from abc import abstractmethod
from dataclasses import dataclass
from typing import Iterable

from read_file.read_file import read_file


class Node:

    @abstractmethod
    def size(self) -> int:
        pass


@dataclass
class Directory(Node):
    name: str
    children: Iterable[Node]

    def size(self) -> int:
        return sum([child.size() for child in self.children])


@dataclass
class File(Node):
    name: str
    file_size: int

    def size(self) -> int:
        return self.file_size


lines = read_file("input.txt")

iterator = iter(lines)
root = Directory("/", [])
stack = [root]
next(iterator)
while True:
    try:
        line = next(iterator)
        current = stack[-1]
        if line.startswith("$ cd"):
            directory_name = line.split(" ")[-1]
            if directory_name == "..":
                stack.pop()
            else:
                directory_to_cd_into = [node for node in current.children if node.name == directory_name][0]
                stack.append(directory_to_cd_into)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            directory_name = line.split(" ")[-1]
            current.children.append(Directory(directory_name, []))
        else:
            file_size, file_name = line.split(" ")
            current.children.append(File(file_name, int(file_size)))
    except StopIteration:
        break


def print_tree(node, depth):
    print(" " * depth, end="")
    if isinstance(node, Directory):
        print(f"- {node.name} (dir)")
        for child in node.children:
            print_tree(child, depth + 1)
    else:
        print(f"- {node.name} (file, size={node.size()})")


def part_1(node):
    if isinstance(node, Directory):
        result = sum([part_1(child) for child in node.children])
        if node.size() <= 100000:
            result += node.size()
        return result
    return 0


remaining_space = 70000000 - root.size()
amount_to_delete = 30000000 - remaining_space


def part_2(node):
    if isinstance(node, Directory):
        smallest_to_delete = min([part_2(child) for child in node.children])
        if amount_to_delete <= node.size() < smallest_to_delete:
            return node.size()
        return smallest_to_delete
    return 99999999999999


print(part_1(root))
print(part_2(root))

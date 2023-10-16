from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Counter

from read_file.read_file import read_file


@dataclass
class Node:
    val: int
    prev: Optional[Node]
    next: Optional[Node]

    def __repr__(self):
        return f"{self.val} {self.prev.val} {self.next.val}"


def parse() -> Node:
    lines = read_file("input.txt")

    head = Node(int(lines[0]), None, None)
    current = head
    for line in lines[1:]:
        node = Node(int(line), None, None)
        current.next = node
        node.prev = current
        current = node
    current.next = head
    head.prev = current
    return head


def calculate_grove_coordinates(head, n_iterations):
    nodes = [head]
    current = head.next
    while current != head:
        nodes.append(current)
        current = current.next

    node_0 = next(node for node in nodes if node.val == 0)

    def remove_from_list(node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left

    def insert_after(node_to_insert_after: Node, node_to_insert: Node):
        node_to_insert_before = node_to_insert_after.next
        node_to_insert_after.next = node_to_insert
        node_to_insert_before.prev = node_to_insert
        node_to_insert.prev = node_to_insert_after
        node_to_insert.next = node_to_insert_before

    for _ in range(n_iterations):
        for node in nodes:
            if not node.val:
                continue
            amount = node.val % (len(nodes) - 1)
            node_to_insert_after = node
            for _ in range(amount):
                node_to_insert_after = node_to_insert_after.next
            remove_from_list(node)
            insert_after(node_to_insert_after, node)

    def value_of_nth_number(n):
        current = node_0
        for _ in range(n):
            current = current.next
        return current.val

    return value_of_nth_number(1000) + value_of_nth_number(2000) + value_of_nth_number(3000)


head_part_1 = parse()
print(calculate_grove_coordinates(head_part_1, 1))

head_part_2 = parse()
current = head_part_2.next
head_part_2.val *= 811589153
while current != head_part_2:
    current.val *= 811589153
    current = current.next

print(calculate_grove_coordinates(head_part_2, 10))

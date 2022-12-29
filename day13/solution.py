import functools

from read_file.read_file import read_file

lines = read_file("input.txt")

iterator = iter(lines)
pairs = []
while True:
    try:
        left = eval(next(iterator))
        right = eval(next(iterator))
        pairs.append((left, right))
        next(iterator)
    except StopIteration:
        break


def is_in_right_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        return -1 if left < right else 1
    if isinstance(left, int):
        return is_in_right_order([left], right)
    if isinstance(right, int):
        return is_in_right_order(left, [right])
    match (left, right):
        case ([], []):
            return 0
        case ([*_], []):
            return 1
        case ([], [*_]):
            return -1
        case ([head_left, *tail_left], [head_right, *tail_right]):
            head_result = is_in_right_order(head_left, head_right)
            if head_result == 0:
                return is_in_right_order(tail_left, tail_right)
            return head_result
    return 1


part_1 = sum(i + 1 for i, pair in enumerate(pairs) if is_in_right_order(*pair) == -1)
print(f"Part 1: {part_1}")

packets = [packet for pair in pairs for packet in pair]
packets += [
    [[2]],
    [[6]],
]

sorted_packets = list(sorted(packets, key=functools.cmp_to_key(is_in_right_order)))
part_2 = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
print(f"Part 2: {part_2}")

from read_file.read_file import read_file

lines = read_file("input.txt")

iterator = iter(lines)
priority_sum = 0
for a, b, c in zip(*[iterator] * 3):
    common = set(a) & set(b) & set(c)
    common_element = common.pop()

    priority = 0
    if common_element.islower():
        priority = 26 - (ord("z") - ord(common_element))
    else:
        priority = 52 - (ord("Z") - ord(common_element))
    priority_sum += priority

print(f"Part 2: {priority_sum}")
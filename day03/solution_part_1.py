from read_file.read_file import read_file

lines = read_file("input.txt")

priority_sum = 0
for line in lines:
    breakpoint = len(line) // 2
    left, right = line[:breakpoint], line[breakpoint:]
    common = set(left) & set(right)
    common_element = common.pop()

    priority = 0
    if common_element.islower():
        priority = 26 - (ord("z") - ord(common_element))
    else:
        priority = 52 - (ord("Z") - ord(common_element))
    print(priority)
    priority_sum += priority

print(f"Part 1: {priority_sum}")
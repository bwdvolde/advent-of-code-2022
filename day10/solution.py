from read_file.read_file import read_file

instructions = read_file("input.txt")

register_value = 1
cycle_values = []
for instruction in instructions:
    if instruction == "noop":
        cycle_values.append(register_value)
    else:
        _, value = instruction.split(" ")
        value = int(value)
        cycle_values.append(register_value)
        register_value += value
        cycle_values.append(register_value)

cycles_of_interest = range(20, 221, 40)
part_1 = sum(cycle_of_interest * cycle_values[cycle_of_interest - 2] for cycle_of_interest in cycles_of_interest)
print(f"Part 1: {part_1}")

print("#", end="")
for cycle in range(1, 240):
    r = cycle // 40
    c = cycle % 40
    if abs(cycle_values[cycle - 1] - c) <= 1:
        print("#", end="")
    else:
        print(".", end="")
    if not (cycle + 1) % 40:
        print()

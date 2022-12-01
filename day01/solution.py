path = "input.txt"

with open(path, "r") as file:
    file_content = file.read()
    unparsed_lines = file_content.split("\n\n")[:-1]
    calories = [sum([int(calories) for calories in line.split("\n")]) for line in unparsed_lines]
    calories.sort()

    print(f"Part 1: {calories[-1]}")
    print(f"Part 2: {sum(calories[-3:])}")

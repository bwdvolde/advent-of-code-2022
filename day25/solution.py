from read_file.read_file import read_file

BASE_CASES = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2",
}


def decimal_to_snafu(number: int) -> str:
    if number in BASE_CASES:
        return BASE_CASES[number]

    length = 0
    total = 2 * (5 ** length)
    while total < abs(number):
        length += 1
        total += 2 * (5 ** length)

    remaining_number = number
    result = ""
    for i in reversed(range(length + 1)):
        division = round(remaining_number / (5 ** i))
        remaining_number = remaining_number - division * (5 ** i)
        result += BASE_CASES[division]
    return result


lines = read_file("input.txt")

total = 0
for line in lines:
    number = 0
    for i, char in enumerate(reversed(line)):
        match char:
            case "0":
                modifier = 0
            case "1":
                modifier = 1
            case "2":
                modifier = 2
            case "-":
                modifier = -1
            case "=":
                modifier = -2

        number += (5 ** i) * modifier
    total += number

print(f"Part 1: {decimal_to_snafu(total)}")

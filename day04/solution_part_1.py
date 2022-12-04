from dataclasses import dataclass

from read_file.read_file import read_file


@dataclass
class Range:
    start: int
    end: int


lines = read_file("input.txt")

n_contained = 0
for line in lines:
    range_unparsed_0, range_unparsed_1 = line.split(",")


    def parse(unparsed) -> Range:
        start, end = unparsed.split("-")
        start, end = int(start), int(end)
        return Range(start, end)


    range_0, range_1 = parse(range_unparsed_0), parse(range_unparsed_1)
    if range_0.start > range_1.start or (range_0.start == range_1.start and range_0.end < range_1.end):
        range_0, range_1 = range_1, range_0

    if range_1.end <= range_0.end:
        n_contained += 1
        print(range_0, range_1, range_1.end <= range_0.end)

print(f"Part 1: {n_contained}")

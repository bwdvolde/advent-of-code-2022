from queue import Queue

from read_file.read_file import read_file

lines = read_file("input.txt")

grid = [list(line) for line in lines]


def calculate_neighbours(r, c):
    possible = [
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1),
    ]
    return [(_r, _c) for (_r, _c) in possible if
            0 <= _r < len(grid) and 0 <= _c < len(grid[_r]) and height(grid[_r][_c]) <= height(grid[r][c]) + 1]


def height(char):
    match char:
        case "S":
            return ord("a")
        case "E":
            return ord("z")
        case _:
            return ord(char)


neighbours = {}

start = None
end = None
for r in range(len(grid)):
    for c in range(len(grid[r])):
        neighbours[(r, c)] = calculate_neighbours(r, c)
        if grid[r][c] == "S":
            start = (r, c)
        elif grid[r][c] == "E":
            end = (r, c)


def calculate_shortest_distance(start):
    queue = Queue()
    queue.put((0, start))
    visited = {start}
    while not queue.empty():
        distance, current = queue.get()
        if current == end:
            return distance
        for neighbour in neighbours[current]:
            if neighbour not in visited:
                queue.put((distance + 1, neighbour))
                visited.add(neighbour)
    return 99999999999


print(f"Part 1: {calculate_shortest_distance(start)}")

starting_positions = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "a"]
part_2 = min(calculate_shortest_distance(starting_position) for starting_position in starting_positions)
print(f"Part 2: {part_2}")

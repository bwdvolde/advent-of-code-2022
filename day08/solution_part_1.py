from read_file.read_file import read_file

lines = read_file("input.txt")

grid = [[int(element) for element in line] for line in lines]

n_visible = 0
for r, row in enumerate(grid):
    for c, el in enumerate(row):
        left = row[:c]
        right = row[c + 1:]
        top = [grid[_r][c] for _r in range(0, r)]
        bottom = [grid[_r][c] for _r in range(r + 1, len(grid))]
        directions = [left, right, top, bottom]
        if any(all(other < el for other in direction) for direction in directions):
            n_visible += 1
print(f"Part 1: {n_visible}")

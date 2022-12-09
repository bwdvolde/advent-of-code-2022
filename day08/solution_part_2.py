from read_file.read_file import read_file

lines = read_file("input.txt")

grid = [[int(element) for element in line] for line in lines]

best_scenic_score = 0
for r, row in enumerate(grid):
    for c, el in enumerate(row):
        left = row[:c][::-1]
        right = row[c + 1:]
        top = [grid[_r][c] for _r in range(0, r)][::-1]
        bottom = [grid[_r][c] for _r in range(r + 1, len(grid))]
        directions = [left, right, top, bottom]
        scenic_score = 1
        for direction in directions:
            viewing_distance = 0
            i = 0
            while i < len(direction):
                viewing_distance += 1
                if direction[i] >= el:
                    break
                i += 1
            scenic_score *= viewing_distance
        best_scenic_score = max(best_scenic_score, scenic_score)
print(f"Part 2: {best_scenic_score}")

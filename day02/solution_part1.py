from read_file.read_file import read_file

lines = read_file("input.txt")
lines = [line.replace("X", "A") for line in lines]
lines = [line.replace("Y", "B") for line in lines]
lines = [line.replace("Z", "C") for line in lines]

scores = 0

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

WINS_FROM = {
    ROCK: SCISSORS,
    SCISSORS: PAPER,
    PAPER: ROCK,
}

score = 0
for line in lines:
    opponent_move, my_move = line.split(" ")
    line_score = 0
    if my_move == opponent_move:
        line_score += 3
    elif WINS_FROM[my_move] == opponent_move:
        line_score += 6

    if my_move == ROCK:
        line_score += 1
    elif my_move == PAPER:
        line_score += 2
    else:
        line_score += 3
    score += line_score

print(f"Part 1: {score}")

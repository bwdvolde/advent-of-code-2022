from read_file.read_file import read_file

lines = read_file("input.txt")

scores = 0

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSE = "X"
DRAW = "Y"
WIN = "Z"

SCORE = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

WINS_FROM = {
    ROCK: SCISSORS,
    SCISSORS: PAPER,
    PAPER: ROCK,
}

LOSES_FROM = {v: k for (k, v) in WINS_FROM.items()}

score = 0
for line in lines:
    opponent_move, desired_outcome = line.split(" ")
    if desired_outcome == LOSE:
        to_play = WINS_FROM[opponent_move]
    elif desired_outcome == DRAW:
        to_play = opponent_move
        score += 3
    else:
        to_play = LOSES_FROM[opponent_move]
        score += 6

    score += SCORE[to_play]

print(f"Part 2: {score}")

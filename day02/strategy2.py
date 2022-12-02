points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

LOSS = 0
DRAW = 3
WIN = 6

input = open("input.txt", "r")
strategy_guide = input.readlines()

score = 0
for i in range(len(strategy_guide)):
    move = strategy_guide[i].split()
    
    if move[1] == "X":      # lose
        score += LOSS + points[lose[move[0]]]
    elif move[1] == "Y":    # draw
        score += DRAW + points[draw[move[0]]]
    else:                   # win
        score += WIN + points[win[move[0]]]

print(score)
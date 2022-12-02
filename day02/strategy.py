points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

enemy_rock = {
    "X": 3,
    "Y": 6,
    "Z": 0
}

enemy_paper = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

enemy_scissor = {
    "X": 6,
    "Y": 0,
    "Z": 3
}

input = open("input.txt", "r")
strategy_guide = input.readlines()

score = 0
for i in range(len(strategy_guide)):
    move = strategy_guide[i].split()
    if move[0] == "A":
        score += enemy_rock[move[1]]
    elif move[0] == "B":
        score += enemy_paper[move[1]]
    else:
        score += enemy_scissor[move[1]]
    score += points.get(move[1])

print(score)
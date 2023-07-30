import json
from datetime import datetime

with open("tmp.txt") as f:
    lines = f.read().split("\n\n")

games = {}

for i in range(0, 1000, 2):
    game = {}

    # moves
    move_parts = lines[i + 1].split()
    moves = []
    for j in range(1, len(move_parts), 3):
        moves.append(move_parts[j])
        moves.append(move_parts[j + 1])

    # metadata
    for l in lines[i].splitlines():
        if l.startswith("[WhiteElo"):
            game["white_rating"] = l.split()[1][1:-2]

        if l.startswith("[BlackElo"):
            game["black_rating"] = l.split()[1][1:-2]

        if l.startswith("[UTCDate"):
            game["date"] = l.split()[1][1:-2]


    game["result"] = move_parts[-1]
    game["moves"] = moves

    games[i // 2 + 1] = game


with open("out.json", "w") as f:
    f.write(json.dumps(games))


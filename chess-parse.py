import json
from datetime import datetime

with open("lichess_db_standard_rated_2013-01.txt") as f:
    lines = f.read().split("\n\n")


games = {}

for i in range(0, 10000, 2):
    game = {}

    # moves
    move_parts = lines[i + 1].split()

    # some games are just weird (have evals)
    if "{" in move_parts:
        continue

    moves = []
    for j in range(1, len(move_parts), 3):
        moves.append(move_parts[j])
        moves.append(move_parts[j + 1])

    # metadata
    game_id = None
    for l in lines[i].splitlines():
        value = l.split()[1][1:-2]

        if l.startswith("[WhiteElo"):
            game["white_rating"] = value

        if l.startswith("[BlackElo"):
            game["black_rating"] = value

        if l.startswith("[UTCDate"):
            game["date"] = value

        if l.startswith("[Site"):
            game_id = value.split("/")[-1]

    if game_id is None:
        continue

    game["result"] = move_parts[-1]
    game["moves"] = moves

    games[game_id] = game

with open("data/sachy.json", "w") as f:
    f.write(json.dumps(games))


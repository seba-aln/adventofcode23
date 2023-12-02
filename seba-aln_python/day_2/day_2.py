import re
from functools import reduce


def solve(data, part):
    return solve_1(data) if part == 1 else solve_2(data)


def get_id(line) -> int:
    return int(line.split(':', 1)[0].replace('Game ', '').strip())


def get_game(line) -> list:
    return [s.strip() for s in re.split(',|;', line.split(':', 1)[1].strip())]


def is_valid(line):
    game_set = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    game = get_game(line)

    for draw in game:
        cnt, color = draw.split()
        if color not in game_set:
            return False
        if game_set[color] < int(cnt):
            return False

    return True


def solve_1(data):
    games = [get_id(line) for line in data if is_valid(line)]
    return sum(games)


def get_cubes(line):
    bag = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for cubes in get_game(line):
        cnt, color = cubes.split()
        bag[color] = max(bag[color], int(cnt))
    print(reduce(lambda a, b: a * b, bag.values()))
    return reduce(lambda a, b: a * b, bag.values())


def solve_2(data):
    games = [get_cubes(line) for line in data]
    return sum(games)

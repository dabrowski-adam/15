import io
from copy import deepcopy
from functools import reduce
from itertools import chain
from typing import List

Puzzle = List[List[int]]


def find_meaning_of_life_the_universe_and_everything() -> int:
    return 42


def swap_puzzle_pieces(puzzle: Puzzle, y1, x1, y2, x2):
    updated_puzzle = deepcopy(puzzle)
    updated_puzzle[y1][x1], updated_puzzle[y2][x2] = updated_puzzle[y2][x2], updated_puzzle[y1][x1]
    return updated_puzzle


def apply_move(puzzle: Puzzle, move: str):
    zero_pos = next(((y, row.index(0)) for y, row in enumerate(puzzle) if 0 in row))
    y1, x1 = zero_pos

    y2, x2 = (y1, x1 + 1) if move == "L" \
        else (y1, x1 - 1) if move == "R" \
        else (y1 + 1, x1) if move == "U" \
        else (y1 - 1, x1)

    max_y = len(puzzle) - 1
    max_x = len(puzzle[0]) - 1

    safe_y2 = min(max(y2, 0), max_y)
    safe_x2 = min(max(x2, 0), max_x)

    return swap_puzzle_pieces(puzzle, y1, x1, safe_y2, safe_x2)


def apply_solution(puzzle: Puzzle, solution: str):
    return reduce(apply_move, solution, puzzle)


def is_solved(puzzle: Puzzle):
    pieces = len(puzzle) * len(puzzle[0])
    solved = [*range(1, pieces), 0]
    return list(chain(*puzzle)) == solved


def check_solution(puzzle: Puzzle, solution: str):
    solved_puzzle = apply_solution(puzzle, solution)
    return is_solved(solved_puzzle)


def count_inversions(puzzle: Puzzle):
    pieces = list(filter(None, chain(*puzzle)))
    length = len(pieces)

    # todo: make it pretty and functional
    inversions = 0
    for i in range(length):
        for j in range(i + 1, length):
            if pieces[i] > pieces[j]:
                inversions += 1

    return inversions


def is_solvable(puzzle: Puzzle):
    n = len(puzzle)
    inversions = count_inversions(puzzle)

    if n % 2 == 1:
        if inversions % 2 == 0:
            return True
    else:
        zero_y = next((y for y, row in enumerate(puzzle) if 0 in row), None)

        if zero_y is None:
            return False

        if zero_y % 2 == 1:
            if inversions % 2 == 0:
                return True
        else:
            if inversions % 2 == 1:
                return True

    return False


def show_solution(solution: str, output: io.TextIOWrapper):
    solution_length = len(solution) if solution is not None else -1
    moves = solution if solution is not None else ""
    output.write(f"{solution_length}\n{moves}")


def show_puzzle(puzzle: Puzzle, output: io.TextIOWrapper):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            output.write(puzzle[y][x])
        output.write("\n")

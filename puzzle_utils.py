import io
from copy import deepcopy
from functools import reduce
from itertools import chain


def find_meaning_of_life_the_universe_and_everything() -> int:
    return 42


def swap_puzzle_pieces(puzzle, y1, x1, y2, x2):
    updated_puzzle = deepcopy(puzzle)
    updated_puzzle[y1][x1], updated_puzzle[y2][x2] = updated_puzzle[y2][x2], updated_puzzle[y1][x1]
    return updated_puzzle


def apply_move(puzzle, move):
    zero_pos, = [(y, row.index(0)) for y, row in enumerate(puzzle) if 0 in row]
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


def apply_solution(puzzle, solution):
    return reduce(apply_move, solution, puzzle)


def is_solved(puzzle):
    pieces = len(puzzle) * len(puzzle[0])
    solved = [*range(1, pieces), 0]
    return list(chain(*puzzle)) == solved


def check_solution(puzzle, solution):
    solved_puzzle = apply_solution(puzzle, solution)
    return is_solved(solved_puzzle)


def show_solution(solution, output: io.TextIOWrapper):
    solution_length = len(solution) if solution is not None else -1
    moves = solution if solution is not None else ""
    output.write(f"{solution_length}\n{moves}")


def show_puzzle(puzzle, output: io.TextIOWrapper):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            output.write(puzzle[y][x])
        output.write("\n")
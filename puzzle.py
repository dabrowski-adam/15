#!/usr/bin/env python3

import sys
import io
from parser import parse
from copy import deepcopy


def bfs(puzzle, order: str):
    return "LRLUDLR"
    #  raise NotImplementedError


def dfs(puzzle, order: str):
    raise NotImplementedError


def idfs(puzzle, order: str):
    raise NotImplementedError


def bf(puzzle, heuristic: int):
    raise NotImplementedError


def astar(puzzle, heuristic: int):
    raise NotImplementedError


def sma(puzzle, heuristic: int):
    raise NotImplementedError


def find_solution(puzzle, strategy, parameter):
    solvers = {
        "bfs": bfs,
        "dfs": dfs,
        "idfs": idfs,
        "bf": bf,
        "astar": astar,
        "sma": sma,
    }

    return solvers[strategy](puzzle, parameter)


def _swap_puzzle_pieces(puzzle, y1, x1, y2, x2):
    updated_puzzle = deepcopy(puzzle)
    updated_puzzle[y1][x1], updated_puzzle[y2][x2] = updated_puzzle[y2][x2], updated_puzzle[y1][x1]
    return updated_puzzle


def apply_move(puzzle, move):
    zero_pos, = [(y, row.index(0)) for y, row in enumerate(puzzle) if 0 in row]
    y1, x1 = zero_pos

    y2, x2 = (y1, x1 + 1) if move == "L"\
        else (y1, x1 - 1) if move == "R"\
        else (y1 + 1, x1) if move == "U"\
        else (y1 - 1, x1)

    max_y = len(puzzle) - 1
    max_x = len(puzzle[0]) - 1

    safe_y2 = min(max(y2, 0), max_y)
    safe_x2 = min(max(x2, 0), max_x)

    return _swap_puzzle_pieces(puzzle, y1, x1, safe_y2, safe_x2)


def apply_solution(puzzle, solution):
    raise NotImplementedError


def show_solution(solution, output: io.TextIOWrapper):
    solution_length = len(solution) if solution is not None else -1
    moves = solution if solution is not None else ""
    output.write(f"{solution_length}\n{moves}")


def show_puzzle(puzzle, output: io.TextIOWrapper):
    output.write("\nSolved puzzle:\n")
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            output.write(puzzle[y][x])
        output.write("\n")


def find_meaning_of_life_the_universe_and_everything() -> int:
    return 42


def main():
    arguments = sys.argv[1:]
    options = parse(arguments)

    puzzle = options["puzzle"]
    strategy = options["strategy"]
    parameter = options["parameter"]
    output: io.TextIOWrapper = options["output"]

    solution = find_solution(puzzle, strategy, parameter)
    show_solution(solution, output)

    #  solved_puzzle = apply_solution(puzzle, solution)
    #  show_puzzle(solved_puzzle, output)

    output.close()


if __name__ == '__main__':
    main()

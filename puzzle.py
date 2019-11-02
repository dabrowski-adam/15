#!/usr/bin/env python3

import io
import sys

from parser import parse
from puzzle_solvers import bfs, dfs, idfs, bf, astar, sma
from puzzle_utils import show_solution


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
    #  output.write("\nSolved puzzle:\n")
    #  show_puzzle(solved_puzzle, output)

    output.close()


if __name__ == "__main__":
    main()

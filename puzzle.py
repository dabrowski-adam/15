#!/usr/bin/env python3

import io
import sys
import time
import os
import psutil

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


def profile(function):
    def profiled(*args, **kwargs):
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        time_before = time.monotonic()

        result = function(*args, **kwargs)

        time_after = time.monotonic()
        memory_after = process.memory_info().rss

        time_diff = (time_after - time_before) * 1000
        memory_diff = (memory_after - memory_before) / 1000

        print(f"Elapsed time: {time_diff} ms\nMemory used: {memory_diff} kB")

        return result

    return profiled


def main():
    arguments = sys.argv[1:]
    options = parse(arguments)

    puzzle = options["puzzle"]
    strategy = options["strategy"]
    parameter = options["parameter"]
    verbose = options["verbose"]
    output: io.TextIOWrapper = options["output"]

    profiled_find_solution = profile(find_solution) if verbose else find_solution
    solution = profiled_find_solution(puzzle, strategy, parameter)
    show_solution(solution, output)

    #  solved_puzzle = apply_solution(puzzle, solution)
    #  output.write("\nSolved puzzle:\n")
    #  show_puzzle(solved_puzzle, output)

    output.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import io
import sys

import kbhit
from parser import parse
from puzzle import find_solution
from puzzle_utils import show_puzzle, apply_solution, Puzzle

kb = kbhit.KBHit()


def delete_last_line():
    "Use this function to delete the last line in the STDOUT"
    sys.stdout.write('\x1b[1A')  # cursor up one line
    sys.stdout.write('\x1b[2K')  # delete last line


def clear(puzzle):
    for i in range(len(puzzle)):
        delete_last_line()


def preview(puzzle: Puzzle, solution: str):
    position = 0
    show_puzzle(puzzle, sys.stdout)
    print(f"\nSolution has {len(solution)} steps.\nPress D to advance, A to go back...")

    while position != len(solution):
        if kb.kbhit():
            key = kb.getch()

            if key == 'd':
                position += 1
            elif key == 'a' and position > 0:
                position -= 1
            else:
                continue

            delete_last_line()
            delete_last_line()
            delete_last_line()
            clear(puzzle)

            moves = solution[:position]
            show_puzzle(apply_solution(puzzle, moves), sys.stdout)

            print("")
            print(f"Step {min(position+1, len(solution))} out of {len(solution)}.")
            print(f"Next move: {solution[position+1]}" if position < len(solution)-1 else "Finished!")

    kb.set_normal_term()


def main():
    arguments = sys.argv[1:]
    options = parse(arguments)

    puzzle = options["puzzle"]
    strategy = options["strategy"]
    parameter = options["parameter"]
    output: io.TextIOWrapper = options["output"]

    solution = find_solution(puzzle, strategy, parameter)
    preview(puzzle, solution)

    output.close()


if __name__ == "__main__":
    main()

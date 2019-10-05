import sys
import io
from parser import parse


def bfs(puzzle, order: str):
    raise NotImplementedError


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


def solve(puzzle, strategy, parameter):
    solvers = {
        "bfs": bfs,
        "dfs": dfs,
        "idfs": idfs,
        "bf": bf,
        "astar": astar,
        "sma": sma,
    }

    return solvers[strategy](puzzle, parameter)


def show(puzzle, output: io.TextIOWrapper):
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

    solved_puzzle = solve(options["puzzle"], options["strategy"], options["parameter"])
    show(solved_puzzle, options["output"])

    options["output"].close()


if __name__ == '__main__':
    main()

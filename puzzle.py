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


def apply_solution(puzzle, solution):
    raise NotImplementedError


def show_solution(solution, strategy, output: io.TextIOWrapper):
    output.write(f"The {strategy} strategy found the following solution:\n{solution}\n")


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
    show_solution(solution, strategy, output)

    #  solved_puzzle = apply_solution(puzzle, solution)
    #  show_puzzle(solved_puzzle, output)

    output.close()


if __name__ == '__main__':
    main()

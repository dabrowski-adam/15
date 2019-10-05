import argparse
import sys
import io


DEFAULT_STRATEGY = ("bfs", "R")


def parse_args(args):
    parser = argparse.ArgumentParser(description="Puzzle solver.", add_help=False)

    parser.add_argument("--input", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--output", type=argparse.FileType("w"), default=sys.stdout)

    parser.add_argument("-b", "--bfs")
    parser.add_argument("-d", "--dfs")
    parser.add_argument("-i", "--idfs")

    parser.add_argument("-h", "--bf", type=int)
    parser.add_argument("-a", "--astar", type=int)
    parser.add_argument("-s", "--sma", type=int)

    return parser.parse_args(args)


def choose_strategy(options):
    strategies = ["bfs", "dfs", "idfs", "bf", "astar", "sma"]
    chosen_strategies = [
        (strategy, options[strategy]) for strategy in strategies if options[strategy]
    ]

    if not chosen_strategies:
        return DEFAULT_STRATEGY

    strategy, *_ = chosen_strategies  # grab the first one
    return strategy


def parse(args):
    options = vars(parse_args(args))
    strategy, parameter = choose_strategy(options)
    standard_input: io.TextIOWrapper = options["input"]
    standard_output: io.TextIOWrapper = options["output"]

    first_line = standard_input.readline()  # two integer values "R C"
    row_count, column_count = [
        int(string) for string in first_line.split()
    ]
    other_lines = [standard_input.readline() for _ in range(row_count)]
    puzzle = [line.split() for line in other_lines]

    return {
        "rows": row_count,
        "columns": column_count,
        "puzzle": puzzle,
        "strategy": strategy,
        "parameter": parameter,
        "output": standard_output,
    }

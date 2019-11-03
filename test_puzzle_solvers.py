import pytest

from puzzle_solvers import bfs, dfs, idfs, bf, astar, sma
from puzzle_utils import check_solution


solvable_puzzle_lul = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 10, 12],
    [13, 14, 11, 15]
]

bfs_test_data = [
    [solvable_puzzle_lul, "LUL"]
]


@pytest.mark.parametrize("puzzle,expected", bfs_test_data)
def test_bfs(puzzle, expected):
    solution = bfs(puzzle, "R")
    assert solution == expected
    assert check_solution(puzzle, solution)

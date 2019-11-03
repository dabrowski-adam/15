import pytest

from puzzle_solvers import bfs, dfs, idfs, bf, astar, sma
from puzzle_utils import check_solution


sample_puzzle = [
    [1, 9, 2, 7],
    [8, 0, 12, 10],
    [13, 3, 6, 4],
    [15, 14, 11, 5]
]

bfs_test_data = [
    [sample_puzzle]
]


@pytest.mark.parametrize("puzzle", bfs_test_data)
def test_bfs(puzzle):
    solution = bfs(puzzle, "R")
    assert check_solution(puzzle, solution)

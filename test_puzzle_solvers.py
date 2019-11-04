import pytest

from puzzle_solvers import bfs, idfs, astar, DIJKSTRA, HAMMING, MANHATTAN
from puzzle_utils import check_solution

solvable_puzzle_lul = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 10, 12],
    [13, 14, 11, 15]
]

solvable_puzzle_rrulul = [
    [1, 2, 3, 4],
    [5, 7, 8, 0],
    [9, 6, 10, 12],
    [13, 14, 11, 15]
]

solvable_puzzle_ddrulu = [
    [1, 3, 5],
    [4, 2, 6],
    [7, 8, 0],
]

test_data = [
    [solvable_puzzle_lul, "LUL"],
    [solvable_puzzle_rrulul, "RRULUL"],
    [solvable_puzzle_ddrulu, "DDRULU"]
]


@pytest.mark.parametrize("puzzle,expected", test_data)
def test_bfs(puzzle, expected):
    solution = bfs(puzzle, "R")
    assert solution == expected
    assert check_solution(puzzle, solution)


@pytest.mark.parametrize("puzzle,expected", test_data)
def test_idfs(puzzle, expected):
    solution = idfs(puzzle, "R")
    assert solution == expected
    assert check_solution(puzzle, solution)


@pytest.mark.parametrize("puzzle,expected", test_data)
def test_astar_dijkstra(puzzle, expected):
    solution = astar(puzzle, DIJKSTRA)
    assert solution == expected
    assert check_solution(puzzle, solution)


@pytest.mark.parametrize("puzzle,expected", test_data)
def test_astar_hamming(puzzle, expected):
    solution = astar(puzzle, HAMMING)
    assert solution == expected
    assert check_solution(puzzle, solution)


@pytest.mark.parametrize("puzzle,expected", test_data)
def test_astar_manhattan(puzzle, expected):
    solution = astar(puzzle, MANHATTAN)
    assert solution == expected
    assert check_solution(puzzle, solution)

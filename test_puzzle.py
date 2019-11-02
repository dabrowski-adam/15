import pytest
from unittest.mock import Mock
from puzzle import find_meaning_of_life_the_universe_and_everything, show_solution, apply_solution, apply_move, \
    swap_puzzle_pieces


def test_find_meaning_of_life_the_universe_and_everything():
    assert find_meaning_of_life_the_universe_and_everything() == 42


show_solution_test_data = [
    (None, "-1\n"),
    ("", "0\n"),
    ("LRUD", "4\nLRUD"),
]


@pytest.mark.parametrize("solution,expected", show_solution_test_data)
def test_show_solution(solution, expected):
    output = Mock()
    show_solution(solution, output)
    output.write.assert_called_with(expected)


sample_puzzle = [
    [1, 9, 2, 7],
    [8, 0, 12, 10],
    [13, 3, 6, 4],
    [15, 14, 11, 5]
]

sample_puzzle_l = [
    [1, 9, 2, 7],
    [8, 12, 0, 10],
    [13, 3, 6, 4],
    [15, 14, 11, 5]
]

sample_puzzle_lurd = [
    [1, 9, 2, 7],
    [8, 0, 6, 10],
    [13, 12, 3, 4],
    [15, 14, 11, 5]
]

sample_puzzle_r = [
    [1, 9, 2, 7],
    [0, 8, 12, 10],
    [13, 3, 6, 4],
    [15, 14, 11, 5]
]

sample_puzzle_u = [
    [1, 9, 2, 7],
    [8, 3, 12, 10],
    [13, 0, 6, 4],
    [15, 14, 11, 5]
]

sample_puzzle_d = [
    [1, 0, 2, 7],
    [8, 9, 12, 10],
    [13, 3, 6, 4],
    [15, 14, 11, 5]
]

apply_solution_test_data = [
    (sample_puzzle, 'LURD', sample_puzzle_lurd),
]


@pytest.mark.parametrize("puzzle,solution,expected", apply_solution_test_data)
def test_apply_solution(puzzle, solution, expected):
    assert apply_solution(puzzle, solution) == expected


apply_move_test_data = [
    (sample_puzzle, 'L', sample_puzzle_l),
    (sample_puzzle, 'R', sample_puzzle_r),
    (sample_puzzle, 'U', sample_puzzle_u),
    (sample_puzzle, 'D', sample_puzzle_d),
]


@pytest.mark.parametrize("puzzle,move,expected", apply_move_test_data)
def test_apply_move(puzzle, move, expected):
    assert apply_move(puzzle, move) == expected


swap_puzzle_pieces_test_data = [
    [sample_puzzle, 1, 2, 1, 1, sample_puzzle_l],
    [sample_puzzle, 1, 0, 1, 1, sample_puzzle_r],
    [sample_puzzle, 2, 1, 1, 1, sample_puzzle_u],
    [sample_puzzle, 0, 1, 1, 1, sample_puzzle_d],
]


@pytest.mark.parametrize("puzzle,y1,x1,y2,x2,expected", swap_puzzle_pieces_test_data)
def test_swap_puzzle_pieces(puzzle, y1, x1, y2, x2, expected):
    assert swap_puzzle_pieces(puzzle, y1, x1, y2, x2) == expected

import pytest
from unittest.mock import Mock
from puzzle import find_meaning_of_life_the_universe_and_everything, show_solution


def test_find_meaning_of_life_the_universe_and_everything():
    assert find_meaning_of_life_the_universe_and_everything() == 42


def test_show_solution_when_impossible_to_solve():
    solution = None
    output = Mock()

    show_solution(solution, output)

    output.write.assert_called_with("-1\n")


def test_show_solution_when_already_solved():
    solution = ""
    output = Mock()

    show_solution(solution, output)

    output.write.assert_called_with("0\n")


def test_show_solution_when_supplied_solution():
    solution = "LRUD"
    output = Mock()

    show_solution(solution, output)

    output.write.assert_called_with("4\nLRUD")

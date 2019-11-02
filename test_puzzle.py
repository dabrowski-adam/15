import pytest
from unittest.mock import Mock
from puzzle import find_meaning_of_life_the_universe_and_everything, show_solution


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

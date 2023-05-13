import pytest
from Challenges.Logic_Challenges.logic_challenges import challenge1

@pytest.mark.parametrize("input, expected", [
  (10, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]),
  (15, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizz buzz"]),
])
def test_challenge1(input, expected):
  assert challenge1(input) == expected
import pytest
from Challenges.Logic_Challenges.logic_challenges import challenge2

@pytest.mark.parametrize("input, expected", [
  (0, 0),
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 3),
  (5, 5),
  (6, 8),
  (7, 13),
  (8, 21),
  (9, 34),
])
def test_challenge2(input, expected):
  assert challenge2(input) == expected


@pytest.mark.parametrize("input", [
  -1,
  -2,
  -3,
  -4,
  -5
])
def test_challenge2_negative(input):
  with pytest.raises(ValueError):
    challenge2(input)
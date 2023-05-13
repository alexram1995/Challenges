import pytest
from Challenges.Logic_Challenges.logic_challenges import challenge3

@pytest.mark.parametrize("input, expected", [
  ("The only thing better than a good game, is a free game", {'a': 2, 'game': 2, 'the': 1, 'only': 1, 'thing': 1, 'better': 1, 'than': 1, 'good': 1, 'is': 1, 'free': 1}),
  ("Well, it’s no secret that the best thing about a secret is secretly telling someone your secret, thereby adding another secret to their secret collection of secrets, secretly", 
    {'secret': 5, 'secretly': 2, 'well': 1, 'it': 1, 's': 1, 'no': 1, 'that': 1, 'the': 1, 'best': 1, 'thing': 1, 'about': 1, 'a': 1, 'is': 1, 'telling': 1, 'someone': 1, 
      'your': 1, 'thereby': 1, 'adding': 1, 'another': 1, 'to': 1, 'their': 1, 'collection': 1, 'of': 1, 'secrets': 1}),
])
def test_challenge3(input, expected):
  assert challenge3(input) == expected
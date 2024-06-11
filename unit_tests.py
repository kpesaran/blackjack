from Hand import Hand
from Card import Card

test_hand = Hand([Card('A','❤️'),Card('A','♣️')])

def test_hand_value() -> bool:
    assert test_hand.check_points() == 12



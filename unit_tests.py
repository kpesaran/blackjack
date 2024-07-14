from Hand import Hand
from Card import Card
from Deck import Deck

test_hand = Hand([Card('A','❤️'),Card('A','♣️')])

def test_hand_value() -> bool:
    # testing if ace value works properly
    assert test_hand.check_points() == 12
def test_hand_bust():
    test_hand = Hand([Card('J', '❤️'), Card('Q', '♣️'), Card('2', '♦️')])
    assert test_hand.check_points() == 22

def test_deck_creation():
    deck = Deck()
    assert deck.count_deck() == 52

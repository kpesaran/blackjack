import random
from Card import Card 

class Deck:
    def __init__ (self):
        self.card_vals = ['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.create_deck()

    def create_deck(self):
        self.deck = []
        for val in self.card_vals:
            for suit in self.suits:
                self.deck.append(Card(val,suit))

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def print_deck(self):
        print(self.deck)


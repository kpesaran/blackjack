import random
from Card import Card 

class Deck:
    def __init__ (self):
        self.card_vals = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.suits = ['❤️','♠️','♣️','♦']
        self.create_deck()

    def create_deck(self):
        """This will create a new instance of a deck"""
        self.__deck = []
        for val in self.card_vals:
            for suit in self.suits:
                self.__deck.append(Card(val,suit))
    def pop(self):
        return self.__deck.pop()

    def shuffle_deck(self):
        random.shuffle(self.__deck)
    
    def print_deck(self):
        print(self.__deck)


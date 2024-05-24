

class Card:
    def __init__(self,val,suit):
        self.suit = suit
        self.val = val 

    def display_card(self):
        return (self.suit, self.val)

    def __str__(self):
        return f"{self.val} of {self.suit}"
    def __repr__(self):
        return self.__str__()


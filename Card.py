# all caps denotes its a contant
ROYALS = ['A','K','Q','J']
class Card:
    
    def __init__(self,val,suit):
        self.suit = suit
        self.val = val 
        if self.val in ROYALS:
            self.point_val = 11
        else:
            self.point_val = int(self.val)

    def display_card(self):
        return (self.suit, self.val)

    def __str__(self):
        return f"{self.val} of {self.suit}"
    def __repr__(self):
        return self.__str__()


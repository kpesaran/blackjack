# all caps denotes its a contant
ROYALS = ['K','Q','J']
class Card:
    """
    
    Used to create a deck of 52 card instances 
    
    """
    def __init__(self,val,suit):
        self.suit = suit
        self.val = val 
        if self.val == 'A':
            self.point_val = 11
        elif self.val in ROYALS:
            self.point_val = 10
        else:
            self.point_val = int(self.val)

    def display_card(self):
        """
        Use this method to display card in UI
        """
        return (self.suit, self.val)

    def __str__(self):
        return f"{self.val} of {self.suit}"

    def __repr__(self):
        return self.__str__()


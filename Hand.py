

class Hand:
    def __init__(self,cards):
        self.cards = cards
        # set up points here

    # move logic into handle the player move...
    
        
    def check_points(self):
        points = 0
        for card in self.cards:
            points += card.point_val 
        # if points > 21:
        #     print(f'gone bust ({points})')
        # elif points == 21:
        #     print('Blackjack!')
        # else:
        #     print(f"Hand is at {points}, hit or stand?")
        
        return points 
    
    def hit(self, card):
        self.cards.append(card)
    
    def print_cards(self):
        return self.cards
        

    
    


    

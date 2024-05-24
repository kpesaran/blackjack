

class Hand:
    def __init__(self,cards):
        self.cards = cards
        # set up points here
        
    def check_cards(self):
        points = 0
        for card in self.cards:
            points += card.val 
        if points > 21:
            print(f'gone bust ({points})')
        elif points == 21:
            print('Blackjack!')
        else:
            print(f"Hand is at {points}, hit or stand?")
    def hit(self, card):
        self.cards.append(card)
        self.check_cards()
    
    

    

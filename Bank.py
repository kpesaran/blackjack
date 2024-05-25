


class Bank:
    def __init__(self, starting_amount):
        self.value = starting_amount
    
    def add_winnings(self, winnings):
        self.value += winnings
    
    def lose_bet(self, losings):
        self.value -= losings
    
    def make_bet(self, amount_bet):
        self.value -= amount_bet
        
    def bank_value(self):
        return self.value

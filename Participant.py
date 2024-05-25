class Participant:
    def __init__(self, hand, bank):
        self.hand = hand
        self.bank = bank
    def print_bank_val(self):
        print(self.bank.value)

class Dealer(Participant):

    def __init__(self, hand, bank):
        super().__init__(hand, bank)
        # Participant.__init__(self, hand)


class Player(Participant):
    
    def __init__(self, hand, bank):
        self.player_bet = 0
        super().__init__(hand, bank)


    def make_bet(self, amount_of_bet):
        if amount_of_bet > self.bank.value:
            raise Exception('Cannot make bet more than your bank value')
        self.player_bet = amount_of_bet
    
    def reset_bet(self):
        self.player_bet = 0
    
    def get_bet(self):
        return self.player_bet
        
        






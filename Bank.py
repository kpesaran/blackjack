class Bank:
    def __init__(self, starting_amount):
        self.__value = starting_amount
    
    def add_winnings(self, winnings):
        self.__value += winnings
    
    def lose_bet(self, losings):
        self.__value -= losings
    
    def make_bet(self, amount_bet):
        self.__value -= amount_bet

        
    def bank_value(self):
        return self.__value

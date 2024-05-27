from Deck import Deck
from Participant import Player, Dealer
from Bank import Bank
from Hand import Hand
import pdb
class Game:
    def __init__(self):
        self.dealer = Dealer(Hand([]), Bank(10000000))
        self.player = Player(Hand([]), Bank(100))
        self.deck = Deck()
        
    
    def check_player_hand(self):
        points = self.player.hand.check_points()
        if points < 21:
            self.handle_player_move()
        
        

    def compare_hands(self):
        player_points = self.player.hand.check_points()
        dealer_points = self.dealer.hand.check_points()
        print('dealer_points: ', dealer_points, 'player_points: ', player_points)
        if player_points > 21:
            self.handle_winner('Dealer')
        elif dealer_points > 21:
            self.handle_winner('Player')
        elif player_points == dealer_points:
            self.handle_winner('Tie')
        elif player_points > dealer_points:
            self.handle_winner('Player')
        else:
            self.handle_winner('Dealer')
    
    

    def handle_winner(self, winner):
        if winner == 'Dealer':
            print('player lost', self.player.get_bet())
        
            self.dealer.bank.add_winnings(self.player.get_bet())
            self.player.bank.lose_bet(self.player.get_bet())
            self.player.reset_bet()
        elif winner == 'Player':
            print('player won', self.player.get_bet())
            self.player.bank.add_winnings(self.player.get_bet())
            self.dealer.bank.lose_bet(self.player.get_bet())
            self.player.reset_bet()
        else:
            print('tie, bet stays on table')
        
    # put into player /dealer 
    def handle_player_move(self):
            # break the logic does a player want another card, and providing the card 
            while self.player.hand.check_points() < 21:
                answer = input('player do you want another card? (y / n)')
                if answer == 'y':
                    self.player.hand.hit(self.deck.deck.pop())
                    print(f'your hand is at:{self.player.hand.check_points()} ')
                else:
                    break
        
    def handle_dealer_move(self):
        points = self.dealer.hand.check_points() 
        while points < 17:
            self.dealer.hand.hit(self.deck.deck.pop())
            
            points = self.dealer.hand.check_points()
        
    def new_round(self):
        self.deck.create_deck()
        self.deck.shuffle_deck()

        number_of_participants = 2
        for i in range(number_of_participants):
            new_hand = []
            for _ in range(2):
                new_hand.append(self.deck.deck.pop())
            if i == 0:
               
                self.dealer.hand.cards = new_hand
            else:
                if self.player.get_bet() == 0:
                    while True:
                        try:
                            bet_amount = input(f'how much do you want to bet(you have ${self.player.bank.bank_value()}? ')
                    
                            self.player.make_bet(int(bet_amount))
                            break
                        except Exception as e: 
                            print(e)
                self.player.hand.cards = new_hand
                

    def start_game(self):
        while self.player.bank.bank_value() > 0 and self.dealer.bank.bank_value() > 0:
            self.new_round()
            print('player cards: ', self.player.hand.print_cards(), 'points: ', self.player.hand.check_points() )
            print('dealer cards: ', self.dealer.hand.print_cards(), 'points: ', self.dealer.hand.check_points())
            self.handle_player_move()
            self.handle_dealer_move()
            self.compare_hands()
            if self.player.bank.bank_value() > 0:
                play_another_round = input('play another round? (y/n)'
                )
                if play_another_round == 'n':
                    break  
            print(self.player.print_bank_val())
# when you have a ton of classes, it adds to many helper values 

#encapsulate as much as possible but also without getting it too complicated 




    
        
    
        

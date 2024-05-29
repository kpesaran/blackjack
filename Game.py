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
        
    def handle_player_move(self, deck, player_hand):
            # break the logic does a player want another card, and providing the card 
            while player_hand.check_points() < 21:
                answer = input('player do you want another card? (y / n)')
                if answer == 'y':
                    player_hand.hit(deck.pop())
                    print(f'your hand is at: {player_hand.check_points()} ')
                    print(player_hand.print_cards())
                else:
                    break
        
    def handle_dealer_move(self, deck, dealer_hand):
        points = self.dealer.hand.check_points() 
        while points < 17:
            self.dealer.hand.hit(deck.pop())
            
            points = dealer_hand.check_points()
        
    def new_round(self, deck):
        deck.create_deck()
        deck.shuffle_deck()

        number_of_participants = 2
        # put players in a list with your dealer at the end of the list 
        for i in range(number_of_participants):
            new_hand = []
            for _ in range(2):
                new_hand.append(deck.pop())
            if i == 0:  
                self.dealer.hand.cards = new_hand
            else:
                if self.player.get_bet() == 0:
                    while True:
                        try:
                            bet_amount = input(f'how much do you want to bet(you have ${self.player.bank.bank_value()})? ')
                    
                            self.player.make_bet(int(bet_amount))
                            break
                        except Exception as e: 
                            print(e)
                self.player.hand.cards = new_hand
                

    def start_game(self):
        while self.player.bank.bank_value() > 0 and self.dealer.bank.bank_value() > 0:
            self.new_round(self.deck)
            print('player cards: ', self.player.hand.print_cards(), 'points: ', self.player.hand.check_points() )
            print('dealer cards: ', self.dealer.hand.print_cards(), 'points: ', self.dealer.hand.check_points())
            self.handle_player_move(self.deck, self.player.hand)
            self.handle_dealer_move(self.deck,self.dealer.hand)
            self.compare_hands()
            if self.player.bank.bank_value() > 0:
                play_another_round = input('play another round? (y/n)'
                )
                if play_another_round == 'n':
                    break  
            print(self.player.print_bank_val())
# when you have a ton of classes, it adds to many helper values 

#encapsulate as much as possible but also without getting it too complicated 




    
        
    
        

import random

# Config options
num_decks = 6;
shuffle_at_perc = 33;
dealer_soft17 = True;

def game(): 
    
    current_deck = []
    def new_deck():
        std_deck = [
    # 2  3  4  5  6  7  8  9  10  J   Q   K   A
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
        ]
        
        # Add number of decks
        deck = std_deck * num_decks
        
        # Shuffle the deck
        random.shuffle(deck)
        
        return deck

    def play_hand():
        dealer_hand = []
        player_hand = []
        
        dealer_hand.append(playing_deck.pop(0))
        player_hand.append(playing_deck.pop(0))
        dealer_hand.append(playing_deck.pop(0))
        player_hand.append(playing_deck.pop(0))
        
        while sum(player_hand) < 17:
            player_hand.append(playing_deck.pop(0))
        
        # While the dealer is on a soft 17, hit, otherwise dealer stands
        while sum(dealer_hand) < 18:
            exit = False
                
            if sum(dealer_hand) == 17: 
                exit = True;
                for i, card in enumerate(dealer_hand):
                    if (card == 11):
                        dealer_hand[i] = 1
                        exit = False;

            if exit:
                break
            
            dealer_hand.append(playing_deck.pop(0))
        
        # Game outcomes: 1. Player wins by getting higher then dealer 2. Player wins by dealer bust 3. Dealer wins by dealer higher than player 4. Dealer wins by player bust 5. Both 21 draw
        # 1=Playerwin, 0=draw, -1=Dealerwin
        
        if sum(player_hand) > 21:
            return -1;
        elif sum(dealer_hand) > 21:
            return 1;
        elif sum(player_hand) > sum(dealer_hand):
            return 1
        elif sum(dealer_hand) > sum(player_hand):
            return -1
        else:
            return 0
        
    playing_deck = new_deck()
    
    wins = 0
    losses = 0
    draws = 0

    games = 10000
    for i in range(0, games):
        
        if (float(len(playing_deck)) / (52 * num_decks)) * 100 < shuffle_at_perc:
            playing_deck = new_deck()
        
        result = play_hand()
        
        if result == 1:
            wins += 1
        if result == 0:
            draws += 1
        if result == -1:
            losses += 1
   
    win_percentage = round((wins / games) * 100, 2)
    lose_percentage = round((losses / games) * 100, 2)
    draw_percentage = round(100 - (win_percentage + lose_percentage), 2)
         
    print('Player wins ->', win_percentage, '%')
    print('Dealer wins ->', lose_percentage, '%')
    print('Draws ->', draw_percentage, '%')
    
game()

# Time to implement basic strategy / card counting

# 1. We need to look at the players cards and the dealers cards therefore, input should take player and dealer hands
# 2. We only see one of the dealers cards so show dealers card at index 0
# 3. Based on the dealers one card and our two cards, we must decide between hit, stand, split or double down


# def basic_strategy(player_hand, dealer_hand):
    
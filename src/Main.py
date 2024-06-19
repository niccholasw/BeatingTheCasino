from NewDeck import new_deck
from PlayGame import play_hand
import Player

# Config options
num_decks = 6
shuffle_at_perc = 75
games = 100000000
    
# Init
playing_deck = new_deck(num_decks)
dealer = Player.Player(1000000000, 0) 
player = Player.Player(1000, 10)

wins = 0
losses = 0
draws = 0

# Main game
try:
    for i in range(0, games):
        if (float(len(playing_deck)) / (52 * num_decks)) * 100 < shuffle_at_perc:
            playing_deck = new_deck(num_decks)
            
        result = play_hand(player, dealer, playing_deck)
        
        if result == 2:
            wins+=1
            player.bal += (player.bet_amount * 1.5)
            # print('win with 21')
        if result == 1:
            wins += 1
            player.bal += player.bet_amount
            # print('win')
        if result == 0:
            draws += 1
            # print('draw')
        if result == -1:
            losses += 1
            player.bal -= player.bet_amount
            # print('lose')
        
        # print('player - >', player.hand)
        # print('dealer - >', dealer.hand)
        
        player.clear_hand()
        dealer.clear_hand()
            
except BaseException as e:
    print(f"Caught an unexpected error: {e}")

# Show stats as a percentage
win_percentage = round((wins / games) * 100, 2)
lose_percentage = round((losses / games) * 100, 2)
draw_percentage = round(100 - (win_percentage + lose_percentage), 2)

print('Player wins ->', win_percentage, '%')
print('Player balance ->', player.bal)
print('Dealer wins ->', lose_percentage, '%')
print('Draws ->', draw_percentage, '%')
print('Games played ->', games)


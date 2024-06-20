from NewDeck import new_deck
from PlayGame import play_hand
import Player
def main():
    # Config options
    num_decks = 6
    shuffle_at_perc = 50
    games = 1000000
        
    # Init
    playing_deck = new_deck(num_decks)
    dealer = Player.Player(1000000000, 0) 
    player = Player.Player(1000, 10)

    gamecount = 0
    try:
        for i in range(0, games):
            if (float(len(playing_deck)) / (52 * num_decks)) * 100 < shuffle_at_perc:
                playing_deck = new_deck(num_decks)
                
            result = play_hand(player, dealer, playing_deck)
            
            player.update_bal(result)
            
            player.clear_hand()
            dealer.clear_hand()
            
            gamecount += 1
            
            if player.bal <= 0:
                # print('Player went bankrupt after', gamecount, 'games.\nThe player never wins...')
                break
                
    except BaseException as e:
        print(f"Caught an unexpected error: {e}")
        
    return gamecount

# Show stats as a percentage
# win_percentage = round((player.wins / gamecount) * 100, 2)
# lose_percentage = round((player.losses / gamecount) * 100, 2)
# draw_percentage = round((player.draws / gamecount) * 100, 2)

# print('Player wins ->', win_percentage, '%')
# print('Dealer wins ->', lose_percentage, '%')
# print('Draws ->', draw_percentage, '%')


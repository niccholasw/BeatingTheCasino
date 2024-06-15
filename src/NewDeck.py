import random

def new_deck(num_decks):
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
    
# playing = new_deck(6)
# print(playing)
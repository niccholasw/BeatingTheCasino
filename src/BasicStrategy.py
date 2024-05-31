
# Time to implement basic strategy / card counting

# 1. We need to look at the players cards and the dealers cards therefore, input should take player and dealer hands
# 2. We only see one of the dealers cards so show dealers card at index 0
# 3. Based on the dealers one card and our two cards, we must decide between hit, stand or double 
# 4. Method returns 0 for stand, 1 for hit and 2 for double
# note: haven't added split yet

def basic_strategy(player_hand, dealer_hand, soft):

    if 4 <= sum(player_hand) <= 8:
        return 1
    if sum(player_hand) == 9:
        if dealer_hand[0] in [2, 7, 8, 9, 10, 11]:
          return 1
        return 2
    if sum(player_hand) == 10:
        if dealer_hand[0] in [10, 11]:
          return 1
        return 2
    if sum(player_hand) == 11:
      return 2
    if soft: # soft is if player has an ace or not
        if sum(player_hand) in [12, 13, 14]:
            if dealer_hand[0] in [5, 6]:
              return 2
            return 1
        if sum(player_hand) in [15, 16]:
            if dealer_hand[0] in [4, 5, 6]:
              return 2
            return 1
        if sum(player_hand) == 17:
            if dealer_hand[0] in [3, 4, 5, 6]:
              return 2
            return 1
        if sum(player_hand) == 18:
            if dealer_hand[0] in [2, 3, 4, 5, 6]:
              return 2
            if dealer_hand[0] in [9, 10, 11]:
              return 1
            return 0
        if sum(player_hand) >= 19:
            return 0

    else:
        if sum(player_hand) == 12:
            if dealer_hand[0] in [2, 3, 7, 8, 9, 10, 11]:
                return 1
            return 0
        if sum(player_hand) in [13, 14, 15, 16]:
            if dealer_hand[0] in [2, 3, 4, 5, 6]:
                return 0
            return 1

        if sum(player_hand) >= 17:
            return 0
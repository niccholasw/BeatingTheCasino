def check_overflow(hand, soft):

    if sum(hand) > 21 & soft:
        for i, card in enumerate(hand):
            if card == 11:
                hand[i] = 1
                for card in hand:
                    if card == 11:
                        soft = True
                        break
                soft = False
    
    return hand, soft
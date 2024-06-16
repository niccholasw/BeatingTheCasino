def check_overflow(hand, soft):
    handchanged = False
    if (sum(hand) > 21) & soft:
        for i, card in enumerate(hand):
            if (card == 11):
                if handchanged:
                    soft = True
                    return hand, soft
                hand[i] = 1
                handchanged = True
        soft = False
    
    return hand, soft
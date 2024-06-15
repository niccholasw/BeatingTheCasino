def play_hand(playing_deck, dealer_soft17):
        soft = False
        dealer_hand = []
        player_hand = []
        
        dealer_hand.append(playing_deck.pop(0))
        player_hand.append(playing_deck.pop(0))
        dealer_hand.append(playing_deck.pop(0))
        player_hand.append(playing_deck.pop(0))
        
        for card in player_hand: 
            if card == 11:
                soft = True;
                
        # Use strategy here
        from BasicStrategy import basic_strategy
        from CheckOverflow import check_overflow
        
        while True:
            play = basic_strategy(player_hand, dealer_hand, soft)
            if play == 1:
                player_hand.append(playing_deck.pop(0))
            elif play == 2:
                player_hand.append(playing_deck.pop(0))
                # bet *= 2
                # break
            elif play == 0:
                # print(player_hand)
                break
            
            player_hand, soft = check_overflow(player_hand, soft)
                  
        
        # While the dealer is on a soft 17, hit, otherwise dealer stands
        while sum(dealer_hand) < 18:
            exit = False
                
            if sum(dealer_hand) == 17 & dealer_soft17: 
                exit = True;
                for i, card in enumerate(dealer_hand):
                    if (card == 11):
                        dealer_hand[i] = 1
                        exit = False;
                        
            elif sum(dealer_hand) >= 16:
                exit = True;
            
            
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
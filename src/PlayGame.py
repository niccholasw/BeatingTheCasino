def play_hand(player, dealer, playing_deck):
        
        player.hand.append(playing_deck.pop(0))
        dealer.hand.append(playing_deck.pop(0))
        player.hand.append(playing_deck.pop(0))
        dealer.hand.append(playing_deck.pop(0))
                
        # Use strategy here
        from BasicStrategy import basic_strategy
        from CheckOverflow import check_overflow
        
        player.is_soft() # Inital check for players aces
        
        while True:
            player.hand, player.soft = check_overflow(player.hand, player.soft)
            
            play = basic_strategy(player.hand, dealer.hand, player.soft)
            if play == 1:
                player.hand.append(playing_deck.pop(0))
            elif play == 2:
                player.hand.append(playing_deck.pop(0))
                player.dd = True
                break
            elif play == 0:
                break

        dealer.is_soft() # Inital check for dealers aces
        dealer.hand, dealer.soft = check_overflow(dealer.hand, dealer.soft) # Check for inital 22 
        
        
        while dealer.get_total() < 17:
            
            dealer.hand.append(playing_deck.pop(0))
            
            dealer.hand, dealer.soft = check_overflow(dealer.hand, dealer.soft)    
            
        
        # Game outcomes: 1. Player wins by getting higher then dealer 2. Player wins by dealer bust 3. Dealer wins by dealer higher than player 4. Dealer wins by player bust 5. Both 21 draw
        # 1=Playerwin, 0=draw, -1=Dealerwin
        
        if player.get_total() > 21:
            return -1
        elif (player.get_total() == 21) & ~(dealer.get_total() == 21):
            return 2
        elif dealer.get_total() > 21:
            return 1
        elif player.get_total() > dealer.get_total():
            return 1
        elif dealer.get_total() > player.get_total():
            return -1
        else:
            return 0
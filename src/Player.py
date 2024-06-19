class Player:
        
    def __init__(self, bal, bet):
        self.hand = []
        self.soft = False
        self.bal = bal
        self.bet = bet
        self.dd = False
        self.wins = 0
        self.draws = 0
        self.losses = 0
        
    def get_total(self):
        return sum(self.hand)
        
    def is_soft(self):
        for card in self.hand: 
            if card == 11:
                self.soft = True
    
    def clear_hand(self):
        self.hand = []
        
    def update_bal(self, win):
        if self.dd:    
            if win == 2:
                self.wins+=1
                self.bal += 2*(self.bet * 1.5)
            if win == 1:
                self.wins += 1
                self.bal += 2*self.bet
            if win == 0:
                self.draws += 1
            if win == -1:
                self.bal -= 2*self.bet
                self.losses += 1
            self.dd = False
            
        else:
            if win == 2:
                self.wins+=1
                self.bal += (self.bet * 1.5)
            if win == 1:
                self.wins += 1
                self.bal += self.bet
            if win == 0:
                self.draws += 1
            if win == -1:
                self.bal -= self.bet
                self.losses += 1
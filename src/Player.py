class Player:
    def __init__(self, bal):
        self.hand = []
        self.soft = False
        self.bal = bal
        
    def get_total(self):
        return sum(self.hand)
        
    def is_soft(self):
        for card in self.hand: 
            if card == 11:
                self.soft = True
    
    def clear_hand(self):
        self.hand = []
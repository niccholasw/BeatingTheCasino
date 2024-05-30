# BeatingTheCasino
Employing Python to run Blackjack strategies to beat the house.

In Blackjack, the house has a natural advantage due to the player always going before the dealer; this advantage can be upwards of 3% sometimes (depending on factors such as the amount of decks, how many decks are played before shuffling etc.). Given a house edge of 3%, the house will win 53% of time, causing players to lose over longer playing sessions. There is however, methods the player can employ to diminish the house edge, and even sometimes gain ad edge over the casino, allowing the player to win over the long run, and rinse these greedy casinos of their money. This project aims to use Python mainly to run machine learning models to test different strategies and help understand which strategy might be the best for the player to gain the greatest edge over the casino.

There are multiple rules for different casinos, however we can generalise most of them to look like this

  1. A common rule is for dealer to stand on all 17s, however, some casinos play hit on soft 17, stand on hard 17
  2. Blackjack (21) -> player wins unless dealer also has Blackjack, pays 3 to 2 in most casinos
  3. Player bust (over 21) -> Player loses entire bet
  4. Dealer bust (over 21) -> Player wins double bet
  5. 





Strategies so far: 

  1. Basic Strategy - Mathematically the best moves
  2. Card Counting - +1 for cards 2-6, 0 for cards 7-9, +1 for cards > 9

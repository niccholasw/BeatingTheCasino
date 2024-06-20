# BeatingTheCasino

Employing Python to run Blackjack strategies to beat the house.

In Blackjack, the house has a natural advantage due to the player always going before the dealer; this advantage can be upwards of 3% sometimes (depending on factors such as the amount of decks, how many decks are played before shuffling etc.). Given a house edge of 3%, the house will win 53% of time, causing players to lose over longer playing sessions. There is however, methods the player can employ to diminish the house edge, and even sometimes gain ad edge over the casino, allowing the player to win over the long run, and rinse these greedy casinos of their money. This project aims to use Python mainly to run machine learning models to test different strategies and help understand which strategy might be the best for the player to gain the greatest edge over the casino.

There are multiple rules for different casinos, however we can generalise most of them to look like this

1. A common rule is for dealer to stand on all 17s, however, some casinos play hit on soft 17, stand on hard 17 will make this changeable, however, we will use stand on all 17 as Aucklnad casino uses this.
2. The amount of standard playing decks used cary from casino to casnio, usually from around 4-8 and the more decks, the more the house wins as the cars are more varied. We will use 6 decks as it is most common, however this can be changed as well in config.
3. Standard plays are hit, stand, split (splitting doubles) and double down (double bet after seeing first two cards, then can only hit once after). Some caisnos allow double down after split.
4. When a player wins they are paid out 2-1 (i.e. 2x their original bet), apart from when they win with BlackJack (21), then they are paid out 3-1 (3x their original bet).
5. Player always hits first, and therefore, if they bust and the dealer also busts, the house still wins.

Strategies so far:

1. Basic Strategy - Mathematically the best moves as proved by mathemiticians over 50 years ago, consists of a table with dealers face card on x axis and players total count on the y axis. Simply look for your corresponding play and play it.
![alt text](assets/basic-resized.png)


2. Card Counting - +1 for cards 2-6, 0 for cards 7-9, -1 for cards > 9 and depending on total count there are more high count cards or low count cards in the deck signifying when to bet more or less.


NOTES: 
Starting bal -> $1000
Bet size -> $10 (fixed for now)

Player wins -> 42.43%
Player balance -> -$15,376,485.0
Dealer wins -> 48.81%
Draws -> 8.76%
Games played -> 100,000,000

This is the stats for player winning with no doubling down or splitting.
This shows that the players expected win rate is 42.43% and clearly over a long period of time they do not expect to win. Without doubling down or splitting, the player is at a significant disadvantage.

By introducing doubling down, the player can bet more money on hands that are more likely to win, which means the player should expect to lose less and even win in some cases as they can leverage better hands to win more.

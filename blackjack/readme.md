**Goal of Blackjack**
The goal of Blackjack (also called 21) is to get a hand value as close to 21 as possible
without going over 21 — while also beating the dealer’s hand.

**Card value**
| Card    | Value                                                                                 |
| ------- | ------------------------------------------------------------------------------------- |
| 2–10    | Face value (2 = 2 points, 10 = 10 points)                                             |
| J, Q, K | 10 points each                                                                        |
| A (Ace) | Can be **1 or 11**, whichever helps your hand most (e.g., 11 unless it causes a bust) |

**Players and Dealer**
The game is played between one or more players and the dealer.
Each player competes only against the dealer, not against other players.

**Starting the Game**
Each player is dealt two cards face up.
The dealer receives two cards — one face up (visible) and one face down (hidden).

**Blackjack (Natural 21)**
If the first two cards total 21 (an Ace + a 10, J, Q, or K), that’s a Blackjack.
Blackjack beats all other hands, even a hand that later totals 21 with more cards.
If both player and dealer have Blackjack → it’s a push (draw).

**Possible moves**
| Move                              | Description                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------- |
| **Hit**                           | Take another card from the deck.                                                             |
| **Stand**                         | Keep your total and end your turn.                                                           |
| **Double Down** *(optional rule)* | Double your bet, take **only one more card**, then stand.                                    |
| **Split** *(optional rule)*       | If your first two cards have the same value (e.g., 8–8), split them into two separate hands. |
| **Surrender** *(optional rule)*   | Forfeit half your bet and stop playing this round.                                           |

In your simplified version, you’ll likely only include Hit and Stand.

**Dealer’s Turn**
After the player finishes, the dealer reveals their hidden card.
The dealer must hit (take another card) until the total is 17 or more.
The dealer must stand once they reach 17 or higher, even if that includes an Ace counted as 11 (called a soft 17 in some rules).

**Bust**
If a player or dealer’s total goes over 21, it’s called a bust — that hand automatically loses.

**Winning Conditions**
| Situation                                                    | Result                   |
| ------------------------------------------------------------ | ------------------------ |
| Player gets 21 (or closest) without busting and beats dealer | ✅ Player wins            |
| Player busts (goes over 21)                                  | ❌ Player loses           |
| Dealer busts, player doesn’t                                 | ✅ Player wins            |
| Both player and dealer have same total                       | 🤝 Draw (push)           |
| Dealer has Blackjack, player doesn’t                         | ❌ Player loses instantly |
| Player has Blackjack, dealer doesn’t                         | 🏆 Player wins instantly |

**Summary of Flow**
Deal two cards to player and dealer.
Check for Blackjack (immediate win/loss).
Player chooses to Hit or Stand.
Dealer reveals and draws until 17+.
Compare scores → decide the winner.
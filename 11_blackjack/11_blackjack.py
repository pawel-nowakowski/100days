from random import shuffle
from blackjack_deck import all_cards_dict as acd


class GameOfBlackjack:
    def __init__(self, cash, cards, bet):
        self.cash = cash
        self.bet = bet
        self.all_cards_dict = cards  # dictionary of cards with their power as value
        self.all_cards = list(cards.keys())  # list of cards by their name
        self.player_cards = []
        self.dealer_cards = []
        self.player_score = 0
        self.dealer_score = 0
        self.player_cards_split = []  # second deck available with split option
        self.player_score_split = 0  # second score available with split option
        self.n = 0  # iterator to draw cards

    # returns cash left of the player
    def cash(self):
        return self.cash

    # draws card and call function to count the score
    def draw_card(self, deck):
        deck.append(self.all_cards[self.n])
        self.n += 1
        if deck == self.player_cards:
            self.player_score_count()
        elif deck == self.player_cards_split:
            self.player_score_count('yes')  # split is active, the function will count the split
        elif deck == self.dealer_cards:
            self.dealer_score_count()
        else:
            print("Incorrect deck has been passed.")
        return deck

    # counts total score, # if any player has an ace and they score above 21,
    # it should change to 1 and recount the score
    def player_score_count(self, split=None):
        if split is None:
            self.player_score += self.all_cards_dict[self.player_cards[-1]]
            if self.player_score > 21:
                if "A♠" in self.player_cards:
                    self.all_cards_dict["A♠"] = 1
                    self.player_score = 0
                elif "A♣" in self.player_cards:
                    self.all_cards_dict["A♣"] = 1
                    self.player_score = 0
                elif "A♥" in self.player_cards:
                    self.all_cards_dict["A♥"] = 1
                    self.player_score = 0
                elif "A♦" in self.player_cards:
                    self.all_cards_dict["A♦"] = 1
                    self.player_score = 0
                if self.player_score == 0:
                    for i in range(len(self.player_cards)):
                        self.player_score += self.all_cards_dict[self.player_cards[-1]]
        else:
            self.player_score_split += self.all_cards_dict[self.player_cards_split[-1]]
            if self.player_score_split > 21:
                if "A♠" in self.player_cards_split:
                    self.all_cards_dict["A♠"] = 1
                    self.player_score_split = 0
                elif "A♣" in self.player_cards_split:
                    self.all_cards_dict["A♣"] = 1
                    self.player_score_split = 0
                elif "A♥" in self.player_cards_split:
                    self.all_cards_dict["A♥"] = 1
                    self.player_score_split = 0
                elif "A♦" in self.player_cards_split:
                    self.all_cards_dict["A♦"] = 1
                    self.player_score_split = 0
                if self.player_score_split == 0:
                    for i in range(len(self.player_cards)):
                        self.player_score_split += self.all_cards_dict[self.player_cards_split[-1]]

    def dealer_score_count(self):
        self.dealer_score += self.all_cards_dict[self.dealer_cards[-1]]
        if self.dealer_score > 21:
            if "A♠" in self.dealer_cards:
                self.all_cards_dict["A♠"] = 1
                self.dealer_score = 0
            elif "A♣" in self.dealer_cards:
                self.all_cards_dict["A♣"] = 1
                self.dealer_score = 0
            elif "A♥" in self.dealer_cards:
                self.all_cards_dict["A♥"] = 1
                self.dealer_score = 0
            elif "A♦" in self.dealer_cards:
                self.all_cards_dict["A♦"] = 1
                self.dealer_score = 0
            if self.dealer_score == 0:
                for i in range(len(self.dealer_cards)):
                    self.dealer_score += self.all_cards_dict[self.dealer_cards[-1]]

    # called when player finishes drawing
    # dealer draws cards till they have less than 17 points, unless player has a blackjack then dealer goes all in
    def dealer_last_stand(self):
        max_score_dealer = 17
        if self.player_score == 21:
            max_score_dealer = 21
        while self.dealer_score < max_score_dealer:
            self.draw_card(self.dealer_cards)
            print(
                f"Dealer draws {self.all_cards[self.n - 1]}. Dealer's cards are now {self.dealer_cards} and he"
                f" has now {self.dealer_score} points.")

    def blackjack(self):
        self.cash -= self.bet
        shuffle(self.all_cards)
        split = False  # default hand is not spli
        game_on = True  # loop for game

        # draw 2 cards for player, 1 for dealer, second is hidden
        self.draw_card(self.player_cards)
        self.draw_card(self.dealer_cards)
        self.draw_card(self.player_cards)

        # allows to do split self.bet if you have a pair
        if self.player_cards[0][0] == self.player_cards[1][0] and self.n == 0:
            split = True

        print(f"Dealer has {self.dealer_cards} and has {self.dealer_score} points.")
        print(f"You have {self.player_cards} and you have {self.player_score} points.")

        print(self.all_cards)  # DELETE
        while game_on:
            action = input(
                (
                    f"What do you want to do?\n Type 'hit', 'stand'{', double down' if len(self.player_cards) == 2 else ''}"
                    f"{', split' if split is True else ''}"
                    f"{', insurance' if 'A' in self.dealer_cards[0] and len(self.dealer_cards) == 1 else ''}: ")).lower()

            # hit -> just get a card
            if action == 'hit':
                if self.dealer_score < 17:
                    self.draw_card(self.dealer_cards)

                self.draw_card(self.player_cards)

                print(f"{self.n} this is n")  # DELETE

                print(
                    f"Dealer draws {self.all_cards[self.n - 2]}. Dealer's cards are now {self.dealer_cards} and he has"
                    f" now {self.dealer_score} points.")
                print(
                    f"You draw {self.all_cards[self.n - 1]}. Your cards are now {self.player_cards} and you have now"
                    f" {self.player_score} points.")

                # stand -> finish getting a cards
            elif action == 'stand' or self.player_score == 21:
                self.dealer_last_stand()

                # double down -> double your self.bet, only possible for the first 2 cards and the next one is the last one.
            elif action == 'double down' and len(self.player_cards) == 2:
                self.cash -= self.bet
                self.bet = 2 * self.bet

                self.draw_card(self.dealer_cards)
                self.draw_card(self.player_cards)

                print(
                    f"Dealer draws {self.all_cards[self.n - 2]}. Dealer's cards are now {self.dealer_cards} and he has now "
                    f"{self.dealer_score} points.")
                print(
                    f"You draw {self.all_cards[self.n - 1]}. Your cards are now {self.player_cards}. You doubled down on "
                    f"your self.bet and you have now {self.player_score} points.")
                self.dealer_last_stand()

                # split -> if you have 2 the same cards, you can split them and take 2 extra self.bets
                # during split you draw cards for both decks
            elif action == 'split' and split is True:
                # during split you hit with your first hand and then second one
                # fix this, it automatically hits both hands

                self.cash -= self.bet

                if self.dealer_score < 17:
                    self.draw_card(self.dealer_cards)

                self.player_cards = self.player_cards[0]
                self.player_cards_split = self.player_cards[1]

                self.draw_card(self.player_cards)
                self.draw_card(self.player_cards_split)

                double_deck_swap = -1  # counter for rounds to swap split decks
                while split:
                    print(
                        f"Dealer draws {self.all_cards[self.n - 3]}. Dealer's cards are now {self.dealer_cards} and he has"
                        f" now {self.dealer_score} points.")
                    print(
                        f"{'You split the hand' if self.n == 6 else ''}\nYour first hand draw is {self.all_cards[self.n - 2]}."
                        f"Your first hand's cards are now {self.player_cards} and your first hand's score is "
                        f" {self.player_cards_split}.\nYour second hand draw is {self.all_cards[self.n - 1]}."
                        f"Your second hand's cards are now {self.player_cards_split} and your first hand's score is "
                        f" {self.player_score_split}. ")
                    action = input(print(f"What do you want to do?\n Type 'hit', 'stand'"))

                    double_deck_swap *= -1
                    if action == 'hit':
                        if double_deck_swap == 1:
                            self.draw_card(self.player_cards)
                        elif double_deck_swap == -1:
                            self.draw_card(self.player_cards_split)

                            # dealer draws card every your second draw since the player has now 2 separate hands
                            if self.dealer_score < 17:
                                self.draw_card(self.dealer_cards)

                    elif action == 'stand':
                        self.dealer_last_stand()
                        split = False
                    else:
                        input("You passed the wrong command.")
                        continue

            elif action == 'insurance' and 'A' in self.dealer_cards[0] and len(self.dealer_cards) == 1:
                self.cash -= self.bet
                print("You have taken an insurance.")
                self.draw_card(self.dealer_cards)
                print(
                    f"Dealer draws {self.all_cards[self.n - 1]}. Dealer's cards are now {self.dealer_cards} and he has"
                    f" now {self.dealer_score} points.")
                if self.dealer_score == 21:
                    print(f"You lost. You take {2 * self.bet}$ for insurance.")
                    self.cash += 2 * self.bet
                else:
                    self.draw_card(self.player_cards)
                    print(
                        f"Dealer draws {self.all_cards[self.n - 2]}. Dealer's cards are now {self.dealer_cards} and he has"
                        f" now {self.dealer_score} points.")
            else:
                print("Incorrect command.")
                continue
            game_on = self.win(action)

        # failcheck, situation should never happen as game of blackjack usually revolves around few first cards
        if self.n > 45:
            print("Deck is running out of cards. Ending the game.")
            return self.cash

        if self.cash == 0:
            print("You don't have any more money.")
        return self.cash

    # win condition
    def win(self, action_command=None):
        game_on = True
        if self.player_score_split != 0:
            if self.player_score > 21:
                score = self.player_score_split
            elif self.player_score_split > 21:
                score = self.player_score
            else:
                if self.player_score > 21 and self.player_score_split > 21:
                    score = min(self.player_score, self.player_score_split)
                else:
                    score = max(self.player_score, self.player_score_split)
        else:
            score = self.player_score

        if score == 21:  # win
            self.cash += self.bet * 2
            print("You hit the blackjack! You won.")
            game_on = False
        elif self.dealer_score > 21:
            print("Dealer hit the blackjack. You lost.")
            game_on = False
        elif score > 21:
            print("You scored above 21 points. You lost.")
            game_on = False
        elif self.dealer_score > 21:  # win
            self.cash += self.bet * 2
            print("Dealer scored above 21 points. You won.")
            game_on = False
        elif score == self.dealer_score:
            self.cash += self.bet
            print(f"You and dealer have {score} points. It's a draw.")
            game_on = False
        elif score > self.dealer_score and action_command == 'stand':
            self.cash += self.bet * 2
            print(f"You have {score} points. You have {score - self.dealer_score} more points. You won.")
            game_on = False
        elif score < self.dealer_score and action_command == 'stand':
            print(f"Dealer has {self.dealer_score} points. You have {self.dealer_score - score} less points. You lost.")
            game_on = False
        return game_on


your_cash = int(input("Type how many $ you want to put into the game of blackjack: "))
bj = GameOfBlackjack(your_cash, acd, 0)
your_cash = bj.cash
print(f"You start with {your_cash}$.")
while your_cash > 0:
    your_bet = input(f"You have {your_cash}$. Type how much you want to bet or type 'exit' to quit: ")
    if your_bet == 'exit':
        print(f"You finish the game with {your_cash}$")
        break
    try:
        your_bet = int(your_bet)
    except:
        print("You have to type a number.")
    if int(your_cash) < your_bet:
        your_bet = your_cash
        print(f"You don't have enough money. Your bet is {your_bet}$.")
    bjInit = GameOfBlackjack(your_cash, acd, your_bet)
    bjInit.blackjack()
    your_cash = bjInit.cash

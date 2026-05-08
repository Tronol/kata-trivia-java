from collections import deque

BOARD_SIZE = 12
WINNING_COINS = 6
QUESTIONS_PER_CATEGORY = 50

CATEGORY_BY_POSITION = {
    0: "Pop", 4: "Pop", 8: "Pop",
    1: "Science", 5: "Science", 9: "Science",
    2: "Sports", 6: "Sports", 10: "Sports",
}


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.coins = 0
        self.in_penalty_box = False

    def advance_to(self, roll):
        self.position += roll
        if self.position > BOARD_SIZE:
            self.position -= BOARD_SIZE

    def add_coin(self):
        self.coins += 1

    def send_to_penalty_box(self):
        self.in_penalty_box = True

    def has_won(self):
        return self.coins == WINNING_COINS


class QuestionDeck:
    CATEGORIES = ["Pop", "Science", "Sports", "Rock"]

    def __init__(self):
        self._questions = {cat: deque() for cat in self.CATEGORIES}
        for i in range(QUESTIONS_PER_CATEGORY):
            self._questions["Pop"].append("Pop Question " + str(i))
            self._questions["Science"].append("Science Question " + str(i))
            self._questions["Sports"].append("Sports Question " + str(i))
            self._questions["Rock"].append("Rock Question " + str(i))

    def ask(self, category):
        print(self._questions[category].popleft())

    def category_for(self, position):
        return CATEGORY_BY_POSITION.get(position - 1, "Rock")


class Game:
    def __init__(self):
        self._players = []
        self._deck = QuestionDeck()

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

    def has_enough_players(self):
        return self.how_many_players() >= 2

    def add(self, player_name):
        self._players.append(Player(player_name))
        print(player_name + " was added")
        print("They are player number " + str(len(self._players)))
        return True

    def how_many_players(self):
        return len(self._players)

    def _current(self):
        return self._players[self.current_player]

    def _advance_position(self, roll):
        self._current().advance_to(roll)
        print(self._current().name + "'s new location is " + str(self._current().position))
        category = self._deck.category_for(self._current().position)
        print("The category is " + category)
        self._deck.ask(category)

    def _advance_turn(self):
        self.current_player += 1
        if self.current_player == len(self._players):
            self.current_player = 0

    def roll(self, roll):
        print(self._current().name + " is the current player")
        print("They have rolled a " + str(roll))

        if not self._current().in_penalty_box:
            self._advance_position(roll)
            return

        leaving_box = roll % 2 != 0
        self.is_getting_out_of_penalty_box = leaving_box
        if leaving_box:
            print(self._current().name + " is getting out of the penalty box")
            self._advance_position(roll)
        else:
            print(self._current().name + " is not getting out of the penalty box")

    def _award_coin_and_check_win(self):
        self._current().add_coin()
        print(self._current().name + " now has " + str(self._current().coins) + " Gold Coins.")
        winner = not self._current().has_won()
        self._advance_turn()
        return winner

    def handle_correct_answer(self):
        if self._current().in_penalty_box:
            if self.is_getting_out_of_penalty_box:
                print("Answer was correct!!!!")
                return self._award_coin_and_check_win()
            else:
                self._advance_turn()
                return True
        else:
            print("Answer was correct!!!!")
            return self._award_coin_and_check_win()

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(self._current().name + " was sent to the penalty box")
        self._current().send_to_penalty_box()
        self._advance_turn()
        return True

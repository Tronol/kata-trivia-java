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
        self.position = 1
        self.coins = 0
        self.in_penalty_box = False


class Game:
    def __init__(self):
        self._players = []

        self.pop_questions = deque()
        self.science_questions = deque()
        self.sports_questions = deque()
        self.rock_questions = deque()

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(QUESTIONS_PER_CATEGORY):
            self.pop_questions.append("Pop Question " + str(i))
            self.science_questions.append("Science Question " + str(i))
            self.sports_questions.append("Sports Question " + str(i))
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question " + str(index)

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
        self._current().position += roll
        if self._current().position > BOARD_SIZE:
            self._current().position -= BOARD_SIZE
        print(self._current().name + "'s new location is " + str(self._current().position))
        print("The category is " + self._current_category())
        self._ask_question()

    def _advance_turn(self):
        self.current_player += 1
        if self.current_player == len(self._players):
            self.current_player = 0

    def roll(self, roll):
        print(self._current().name + " is the current player")
        print("They have rolled a " + str(roll))

        if self._current().in_penalty_box:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True
                print(self._current().name + " is getting out of the penalty box")
                self._advance_position(roll)
            else:
                print(self._current().name + " is not getting out of the penalty box")
                self.is_getting_out_of_penalty_box = False
        else:
            self._advance_position(roll)

    def _ask_question(self):
        category = self._current_category()
        questions = {
            "Pop": self.pop_questions,
            "Science": self.science_questions,
            "Sports": self.sports_questions,
            "Rock": self.rock_questions,
        }
        print(questions[category].popleft())

    def _current_category(self):
        pos = self._current().position - 1
        return CATEGORY_BY_POSITION.get(pos, "Rock")

    def _award_coin_and_check_win(self):
        self._current().coins += 1
        print(self._current().name + " now has " + str(self._current().coins) + " Gold Coins.")
        winner = self._did_player_win()
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
            print("Answer was corrent!!!!")
            return self._award_coin_and_check_win()

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(self._current().name + " was sent to the penalty box")
        self._current().in_penalty_box = True
        self._advance_turn()
        return True

    def _did_player_win(self):
        return not (self._current().coins == WINNING_COINS)

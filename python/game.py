from collections import deque

BOARD_SIZE = 12
WINNING_COINS = 6
QUESTIONS_PER_CATEGORY = 50


class Game:
    def __init__(self):
        self.players = []
        self._player_positions = [0] * 6
        self._player_coins = [0] * 6
        self.in_penalty_box = [False] * 6

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
        idx = self.how_many_players()
        self._player_positions[idx] = 1
        self._player_coins[idx] = 0
        self.in_penalty_box[idx] = False
        self.players.append(player_name)
        print(player_name + " was added")
        print("They are player number " + str(len(self.players)))
        return True

    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print(self.players[self.current_player] + " is the current player")
        print("They have rolled a " + str(roll))

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True
                print(self.players[self.current_player] + " is getting out of the penalty box")
                self._player_positions[self.current_player] = self._player_positions[self.current_player] + roll
                if self._player_positions[self.current_player] > BOARD_SIZE:
                    self._player_positions[self.current_player] = self._player_positions[self.current_player] - BOARD_SIZE
                print(self.players[self.current_player] + "'s new location is " + str(self._player_positions[self.current_player]))
                print("The category is " + self._current_category())
                self._ask_question()
            else:
                print(self.players[self.current_player] + " is not getting out of the penalty box")
                self.is_getting_out_of_penalty_box = False
        else:
            self._player_positions[self.current_player] = self._player_positions[self.current_player] + roll
            if self._player_positions[self.current_player] > BOARD_SIZE:
                self._player_positions[self.current_player] = self._player_positions[self.current_player] - BOARD_SIZE
            print(self.players[self.current_player] + "'s new location is " + str(self._player_positions[self.current_player]))
            print("The category is " + self._current_category())
            self._ask_question()

    def _ask_question(self):
        if self._current_category() == "Pop":
            print(self.pop_questions.popleft())
        if self._current_category() == "Science":
            print(self.science_questions.popleft())
        if self._current_category() == "Sports":
            print(self.sports_questions.popleft())
        if self._current_category() == "Rock":
            print(self.rock_questions.popleft())

    def _current_category(self):
        if self._player_positions[self.current_player] - 1 == 0: return "Pop"
        if self._player_positions[self.current_player] - 1 == 4: return "Pop"
        if self._player_positions[self.current_player] - 1 == 8: return "Pop"
        if self._player_positions[self.current_player] - 1 == 1: return "Science"
        if self._player_positions[self.current_player] - 1 == 5: return "Science"
        if self._player_positions[self.current_player] - 1 == 9: return "Science"
        if self._player_positions[self.current_player] - 1 == 2: return "Sports"
        if self._player_positions[self.current_player] - 1 == 6: return "Sports"
        if self._player_positions[self.current_player] - 1 == 10: return "Sports"
        return "Rock"

    def handle_correct_answer(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print("Answer was correct!!!!")
                self._player_coins[self.current_player] += 1
                print(self.players[self.current_player] + " now has " + str(self._player_coins[self.current_player]) + " Gold Coins.")
                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                return True
        else:
            print("Answer was corrent!!!!")
            self._player_coins[self.current_player] += 1
            print(self.players[self.current_player] + " now has " + str(self._player_coins[self.current_player]) + " Gold Coins.")
            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players):
                self.current_player = 0
            return winner

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self._player_coins[self.current_player] == WINNING_COINS)

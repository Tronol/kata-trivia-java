import random
import io
import contextlib

from game import Game
from game_old import GameOld


def _run_game(seed, game_factory):
    rand = random.Random(seed)
    game = game_factory()
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        game.add("Chet")
        game.add("Pat")
        game.add("Sue")
        while True:
            game.roll(rand.randint(1, 5))
            if rand.randint(0, 8) == 7:
                not_a_winner = game.wrong_answer()
            else:
                not_a_winner = game.handle_correct_answer()
            if not not_a_winner:
                break
    return output.getvalue()


def test_golden_master():
    for seed in range(1, 10_001):
        expected = _run_game(seed, GameOld)
        actual = _run_game(seed, Game)
        assert actual == expected, f"Change detected for seed {seed}"

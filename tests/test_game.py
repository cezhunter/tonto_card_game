# Copyright (c) 2021 Cezanne Vahid

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from random import Random

import pytest

from tonto.card import Card
from tonto.deck import Deck
from tonto.exception import GameError
from tonto.game import Game

MESSAGE = {
    "WELCOME": ["Welcome."],
    "ROUND START": ["Round $current_round."],
    "ROUND END": ["$round_winner won the round."],
    "ROUND END TIE": ["Round was a tie."],
    "TURN START": ["$current_player_name turn."],
    "FALSE TURN END": [
        ("Negative, $current_player_name drew $current_card "
         "bringing score to $current_player_score.")
    ],
    "TRUE TURN END": [
        ("Positive, $current_player_name drew $current_card "
         "bringing score to $current_player_score.")
    ],
    "GAME OVER TIE": ["Game was a tie."],
    "GAME OVER": ["Game over, $game_winner won."],
    "EMPTY DECK": ["Deck empty."],
}

GAME_1_RESULTS = ("Welcome.\nRound 1.\nBerkelly turn.\n"
                  "Positive, Berkelly drew 10 of Spades "
                  "bringing score to 10.\nBerkelly won the round.\n"
                  "Game over, Berkelly won.\n1: Berkelly (10)\n")

GAME_2_RESULTS = ("Welcome.\nRound 1.\nBerkelly turn.\n"
                  "Positive, Berkelly drew King of Spades bringing "
                  "score to 13.\nBerkelly won the round.\nGame over, "
                  "Berkelly won.\n1: Berkelly (13)\n")

GAME_3_RESULTS = ("Welcome.\nRound 1.\nBerkelly turn.\n"
                  "Positive, Berkelly drew 9 of Clubs bringing score to 36.\n"
                  "Berkelly won the round.\nRound 2.\nBerkelly turn.\nDeck "
                  "empty.\nPositive, Berkelly drew 10 of Spades bringing "
                  "score to 46.\nBerkelly won the round.\nGame over, "
                  "Berkelly won.\n1: Berkelly (46)\n")

GAME_4_RESULTS = ("Welcome.\nRound 1.\nBerkelly turn.\nPositive, Berkelly "
                  "drew 10 of Spades bringing score to 10.\nCez turn."
                  "\nPositive, Cez drew Queen of Hearts bringing score to 36."
                  "\nTonto turn.\nPositive, Tonto drew Jack of Clubs "
                  "bringing score to 44.\nTonto won the round.\nRound 2.\n"
                  "Berkelly turn.\nNegative, Berkelly drew 6 of Spades "
                  "bringing score to 16.\nCez turn.\nPositive, Cez drew 5 "
                  "of Diamonds bringing score to 46.\nTonto turn.\nPositive, "
                  "Tonto drew 9 of Spades bringing score to 53.\nCez won the "
                  "round.\nRound 3.\nBerkelly turn.\nNegative, Berkelly drew "
                  "7 of Hearts bringing score to 37.\nCez turn.\nPositive, "
                  "Cez drew 4 of Hearts bringing score to 58.\nTonto turn."
                  "\nPositive, Tonto drew 6 of Hearts bringing score to 71."
                  "\nBerkelly won the round.\nGame over, Tonto won.\n1: "
                  "Tonto (71)\n2: Cez (58)\n3: Berkelly (37)\n")

GAME_5_RESULTS = ("Welcome.\nRound 1.\nBerkelly turn.\nPositive, Berkelly drew"
                  " 10 of Spades bringing score to 10.\nCez turn.\nNegative, "
                  "Cez drew 3 of Diamonds bringing score to 6.\nTonto turn."
                  "\nPositive, Tonto drew 5 of Diamonds bringing score to 10."
                  "\nRound was a tie.\nRound 2.\nBerkelly turn.\nPositive, "
                  "Berkelly drew King of Spades bringing score to 23.\nCez "
                  "turn.\nPositive, Cez drew Ace of Clubs bringing score to "
                  "62.\nTonto turn.\nNegative, Tonto drew 9 of Clubs "
                  "bringing score to 46.\nCez won the round.\nRound 3."
                  "\nBerkelly turn.\nNegative, Berkelly drew 3 of Diamonds "
                  "bringing score to 29.\nCez turn.\nPositive, Cez drew 8 "
                  "of Spades bringing score to 70.\nTonto turn.\nPositive, "
                  "Tonto drew 6 of Clubs bringing score to 70.\nTonto won "
                  "the round.\nGame was a tie.\n1: Cez (70)\n1: Tonto (70)"
                  "\n2: Berkelly (29)\n")

PLAYERS_1 = ["Berkelly"]
PLAYERS_2 = ["Berkelly", "Cez", "Tonto"]

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"


def test_basic_game_1(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "")

    with pytest.raises(GameError):
        Game([])
    with pytest.raises(GameError):
        Game(PLAYERS_1, max_rounds=0)
    game = Game(PLAYERS_1)
    assert game
    game.play()
    assert not game
    game.new_game()
    assert game


def test_basic_game_2(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "")

    rand = Random()
    rand.seed(1)
    deck = Deck(random_instance=rand)
    deck.shuffle()

    game = Game(PLAYERS_1, deck=deck, message=MESSAGE, max_rounds=1)
    assert game
    game.play()
    assert not game
    captured = capsys.readouterr()
    assert captured.out == GAME_1_RESULTS

    game.new_game()
    assert game
    game.play()
    assert not game
    captured = capsys.readouterr()
    assert captured.out == GAME_2_RESULTS


def test__basic_game_3(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "")

    rand = Random()
    rand.seed(1)
    deck = Deck(empty=True, random_instance=rand)
    deck.add_card(Card("Clubs", "9"))
    deck.shuffle()

    game = Game(PLAYERS_1, deck=deck, message=MESSAGE, max_rounds=2)
    game.play()
    captured = capsys.readouterr()
    assert captured.out == GAME_3_RESULTS


def test_basic_game_4(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "")

    rand = Random()
    rand.seed(1)
    deck = Deck(random_instance=rand)
    deck.shuffle()

    game = Game(PLAYERS_2, deck=deck, message=MESSAGE)
    game.play()
    captured = capsys.readouterr()
    assert captured.out == GAME_4_RESULTS


def test_basic_game_5(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "")

    cards = [
        Card("Clubs", "6"),
        Card("Spades", "8"),
        Card("Diamonds", "3"),
        Card("Clubs", "9"),
        Card("Clubs", "Ace"),
        Card("Spades", "King"),
        Card("Diamonds", "5"),
        Card("Diamonds", "3"),
        Card("Spades", "10"),
    ]
    deck = Deck(empty=True)
    for card in cards:
        deck.add_card(card)
    game = Game(PLAYERS_2, deck=deck, message=MESSAGE)
    game.play()
    captured = capsys.readouterr()
    assert captured.out == GAME_5_RESULTS

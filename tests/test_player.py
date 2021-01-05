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

import pytest

from tonto.card import Card
from tonto.deck import Deck
from tonto.exception import InvalidCardError, InvalidPlayerError
from tonto.player import Player, Players

STRING_1 = "Berkelly holds [] totalling 0 points"
STRING_2 = "Berkelly holds [('Clubs', 'King')] totalling 52 points"
STRING_3 = ("Berkelly holds [('Clubs', 'King'), ('Hearts', '8')] "
            "totalling 76 points")

LEADERBOARD_1 = "1: Berkelly (0)"
LEADERBOARD_2 = "1: Berkelly (36)"
LEADERBOARD_3 = "1: Berkelly (69)"
LEADERBOARD_4 = "1: Berkelly (0)\n1: Cez (0)"
LEADERBOARD_5 = "1: Cez (12)\n2: Berkelly (0)"
LEADERBOARD_6 = "1: Berkelly (12)\n1: Cez (12)"
LEADERBOARD_7 = "1: Berkelly (25)\n2: Cez (12)"
LEADERBOARD_8 = "1: Berkelly (56)\n2: Cez (10)\n2: Tonto (10)"

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"

def test_basic_player_1():
    with pytest.raises(TypeError):
        player_1 = Player()

    deck = Deck(empty=True)
    player_1 = Player("Berkelly")
    assert player_1.name == "Berkelly"
    assert player_1.hand == deck
    assert str(player_1.hand) == str(deck)
    assert player_1.score() == 0
    assert not player_1.score(round_number=1)
    assert str(player_1) == STRING_1

    card_1 = Card("Clubs", "King")
    deck.add_card(card_1)
    player_1.draw_card(card_1)
    assert player_1.hand == deck
    assert str(player_1.hand) == str(deck)
    assert player_1.score() == 52
    assert player_1.score(round_number=1) == 52
    assert str(player_1) == STRING_2

    card_2 = Card("Hearts", "8")
    deck.add_card(card_2)
    player_1.draw_card(card_2)
    assert player_1.hand == deck
    assert str(player_1.hand) == str(deck)
    assert player_1.score() == 76
    assert player_1.score(round_number=1) == 52
    assert player_1.score(round_number=2) == 24
    assert str(player_1) == STRING_3

    assert player_1.hand == deck
    assert str(player_1.hand) == str(deck)
    assert player_1.score() == 76
    assert player_1.score(round_number=1) == 52
    assert player_1.score(round_number=2) == 24
    assert str(player_1) == STRING_3

    deck = Deck(empty=True)
    player_1.clear_hand()
    assert player_1.name == "Berkelly"
    assert player_1.hand == deck
    assert str(player_1.hand) == str(deck)
    assert player_1.score() == 0
    assert not player_1.score(round_number=1)
    assert str(player_1) == STRING_1

    player_1.draw_card(card_1)
    player_1.draw_card(card_2)
    player_2 = Player("Cez")
    assert player_1 > player_2
    assert player_2 < player_1

    card_1 = Card("Diamonds", "8")
    card_2 = Card("Clubs", "2")
    player_2.draw_card(card_1)
    player_2.draw_card(card_2)
    assert player_1 > player_2
    assert player_2 < player_1

    player_1 = Player("Cez")
    player_1.draw_card(card_1)
    player_1.draw_card(card_2)
    assert player_1 == player_2

    player_1 = Player("Cez")
    player_1.draw_card(card_2)
    assert player_1 != player_2


def test_basic_player_2():
    players = Players([])
    assert len(players) == 0
    assert not players.first().name
    assert not players.first(round_number=1).name
    with pytest.raises(StopIteration):
        next(players)
    assert str(players) == ""

    with pytest.raises(InvalidPlayerError):
        players = Players(["first"])

    players = Players(["Berkelly"])
    player = Player("Berkelly")
    assert players.Berkelly == player
    assert len(players) == 1
    assert next(players) == player
    assert players[0] == player
    assert not players.first().tie
    assert players.first().player == player
    assert not players.second().name
    assert str(players) == LEADERBOARD_1

    players.reset()
    assert players.Berkelly == player
    assert len(players) == 1
    assert next(players) == player
    assert players[0] == player
    assert not players.first().tie
    assert players.first().player == player
    assert not players.second().name
    assert str(players) == LEADERBOARD_1

    players.Berkelly.draw_card(Card("Clubs", "9"))
    player.draw_card(Card("Clubs", "9"))
    assert not players.first().tie
    assert players.first().player == player
    assert not players.second().name
    assert str(players) == LEADERBOARD_2

    players.Berkelly.draw_card(Card("Hearts", "Jack"))
    player.draw_card(Card("Hearts", "Jack"))
    assert not players.first().tie
    assert players.first().player == player
    assert not players.second().name
    assert str(players) == LEADERBOARD_3

def test_basic_player_3():
    players = Players(["Berkelly", "Cez"])
    player_1 = Player("Berkelly")
    player_2 = Player("Cez")
    assert len(players) == 2
    assert players.first().tie
    assert player_1 in players.first().players
    assert player_2 in players.first().players
    assert str(players) == LEADERBOARD_4

    players.Cez.draw_card(Card("Clubs", "3"))
    player_2.draw_card(Card("Clubs", "3"))
    assert not players.first().tie
    assert players.first().player == player_2
    assert players.first().name == player_2.name
    assert players.first().score == 12
    assert players.second().player == player_1
    assert players.second().name == player_1.name
    assert players.second().score == 0
    assert str(players) == LEADERBOARD_5

    players.Berkelly.draw_card(Card("Hearts", "4"))
    player_1.draw_card(Card("Hearts", "4"))
    assert players.first().tie
    assert player_1 in players.first().players
    assert player_1.name in players.first().names
    assert player_2 in players.first().players
    assert player_2.name in players.first().names
    assert players.first().score == 12
    assert str(players) == LEADERBOARD_6

    players.Berkelly.draw_card(Card("Spades", "King"))
    player_1.draw_card(Card("Spades", "King"))
    assert not players.first().tie
    assert players.first().player == player_1
    assert players.first().name == player_1.name
    assert players.first().score == 25
    assert players.second().player == player_2
    assert players.second().name == player_2.name
    assert players.second().score == 12
    assert str(players) == LEADERBOARD_7

    assert players.first(1).tie
    assert not players.first(2).tie
    assert players.first(2).player == player_1
    assert players.first(2).name == player_1.name

    players = Players(["Berkelly", "Cez", "Tonto"])
    players.Berkelly.draw_card(Card("Clubs", "Ace"))
    players.Tonto.draw_card(Card("Diamonds", "5"))
    players.Cez.draw_card(Card("Spades", "10"))
    assert str(players) == LEADERBOARD_8

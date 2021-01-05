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
from tonto.exception import DeckEmptyError, InvalidCardError

UNSHUFFLED_DECK = [
    Card("Spades", "2"),
    Card("Spades", "3"),
    Card("Spades", "4"),
    Card("Spades", "5"),
    Card("Spades", "6"),
    Card("Spades", "7"),
    Card("Spades", "8"),
    Card("Spades", "9"),
    Card("Spades", "10"),
    Card("Spades", "Jack"),
    Card("Spades", "Queen"),
    Card("Spades", "King"),
    Card("Spades", "Ace"),
    Card("Diamonds", "2"),
    Card("Diamonds", "3"),
    Card("Diamonds", "4"),
    Card("Diamonds", "5"),
    Card("Diamonds", "6"),
    Card("Diamonds", "7"),
    Card("Diamonds", "8"),
    Card("Diamonds", "9"),
    Card("Diamonds", "10"),
    Card("Diamonds", "Jack"),
    Card("Diamonds", "Queen"),
    Card("Diamonds", "King"),
    Card("Diamonds", "Ace"),
    Card("Hearts", "2"),
    Card("Hearts", "3"),
    Card("Hearts", "4"),
    Card("Hearts", "5"),
    Card("Hearts", "6"),
    Card("Hearts", "7"),
    Card("Hearts", "8"),
    Card("Hearts", "9"),
    Card("Hearts", "10"),
    Card("Hearts", "Jack"),
    Card("Hearts", "Queen"),
    Card("Hearts", "King"),
    Card("Hearts", "Ace"),
    Card("Clubs", "2"),
    Card("Clubs", "3"),
    Card("Clubs", "4"),
    Card("Clubs", "5"),
    Card("Clubs", "6"),
    Card("Clubs", "7"),
    Card("Clubs", "8"),
    Card("Clubs", "9"),
    Card("Clubs", "10"),
    Card("Clubs", "Jack"),
    Card("Clubs", "Queen"),
    Card("Clubs", "King"),
    Card("Clubs", "Ace"),
]

UNSHUFFLED_DECK_TUPLES = [
    ("Spades", "2"),
    ("Spades", "3"),
    ("Spades", "4"),
    ("Spades", "5"),
    ("Spades", "6"),
    ("Spades", "7"),
    ("Spades", "8"),
    ("Spades", "9"),
    ("Spades", "10"),
    ("Spades", "Jack"),
    ("Spades", "Queen"),
    ("Spades", "King"),
    ("Spades", "Ace"),
    ("Diamonds", "2"),
    ("Diamonds", "3"),
    ("Diamonds", "4"),
    ("Diamonds", "5"),
    ("Diamonds", "6"),
    ("Diamonds", "7"),
    ("Diamonds", "8"),
    ("Diamonds", "9"),
    ("Diamonds", "10"),
    ("Diamonds", "Jack"),
    ("Diamonds", "Queen"),
    ("Diamonds", "King"),
    ("Diamonds", "Ace"),
    ("Hearts", "2"),
    ("Hearts", "3"),
    ("Hearts", "4"),
    ("Hearts", "5"),
    ("Hearts", "6"),
    ("Hearts", "7"),
    ("Hearts", "8"),
    ("Hearts", "9"),
    ("Hearts", "10"),
    ("Hearts", "Jack"),
    ("Hearts", "Queen"),
    ("Hearts", "King"),
    ("Hearts", "Ace"),
    ("Clubs", "2"),
    ("Clubs", "3"),
    ("Clubs", "4"),
    ("Clubs", "5"),
    ("Clubs", "6"),
    ("Clubs", "7"),
    ("Clubs", "8"),
    ("Clubs", "9"),
    ("Clubs", "10"),
    ("Clubs", "Jack"),
    ("Clubs", "Queen"),
    ("Clubs", "King"),
    ("Clubs", "Ace"),
]

SHUFFLED_DECK_1 = [
    Card("Clubs", "Queen"),
    Card("Spades", "Jack"),
    Card("Hearts", "King"),
    Card("Diamonds", "Jack"),
    Card("Spades", "4"),
    Card("Hearts", "Ace"),
    Card("Diamonds", "8"),
    Card("Spades", "King"),
    Card("Hearts", "Jack"),
    Card("Spades", "7"),
    Card("Hearts", "5"),
    Card("Clubs", "Ace"),
    Card("Clubs", "6"),
    Card("Diamonds", "4"),
    Card("Diamonds", "Queen"),
    Card("Clubs", "9"),
    Card("Clubs", "10"),
    Card("Diamonds", "10"),
    Card("Clubs", "3"),
    Card("Clubs", "2"),
    Card("Spades", "Ace"),
    Card("Clubs", "King"),
    Card("Hearts", "8"),
    Card("Diamonds", "9"),
    Card("Diamonds", "Ace"),
    Card("Hearts", "2"),
    Card("Hearts", "10"),
    Card("Spades", "Queen"),
    Card("Hearts", "9"),
    Card("Spades", "5"),
    Card("Diamonds", "7"),
    Card("Diamonds", "3"),
    Card("Diamonds", "6"),
    Card("Clubs", "7"),
    Card("Spades", "2"),
    Card("Hearts", "3"),
    Card("Clubs", "5"),
    Card("Spades", "3"),
    Card("Clubs", "8"),
    Card("Spades", "8"),
    Card("Diamonds", "2"),
    Card("Diamonds", "King"),
    Card("Clubs", "4"),
    Card("Hearts", "6"),
    Card("Hearts", "4"),
    Card("Hearts", "7"),
    Card("Spades", "9"),
    Card("Diamonds", "5"),
    Card("Spades", "6"),
    Card("Clubs", "Jack"),
    Card("Hearts", "Queen"),
    Card("Spades", "10"),
]

SHUFFLED_DECK_1_TUPLES = [
    ("Clubs", "Queen"),
    ("Spades", "Jack"),
    ("Hearts", "King"),
    ("Diamonds", "Jack"),
    ("Spades", "4"),
    ("Hearts", "Ace"),
    ("Diamonds", "8"),
    ("Spades", "King"),
    ("Hearts", "Jack"),
    ("Spades", "7"),
    ("Hearts", "5"),
    ("Clubs", "Ace"),
    ("Clubs", "6"),
    ("Diamonds", "4"),
    ("Diamonds", "Queen"),
    ("Clubs", "9"),
    ("Clubs", "10"),
    ("Diamonds", "10"),
    ("Clubs", "3"),
    ("Clubs", "2"),
    ("Spades", "Ace"),
    ("Clubs", "King"),
    ("Hearts", "8"),
    ("Diamonds", "9"),
    ("Diamonds", "Ace"),
    ("Hearts", "2"),
    ("Hearts", "10"),
    ("Spades", "Queen"),
    ("Hearts", "9"),
    ("Spades", "5"),
    ("Diamonds", "7"),
    ("Diamonds", "3"),
    ("Diamonds", "6"),
    ("Clubs", "7"),
    ("Spades", "2"),
    ("Hearts", "3"),
    ("Clubs", "5"),
    ("Spades", "3"),
    ("Clubs", "8"),
    ("Spades", "8"),
    ("Diamonds", "2"),
    ("Diamonds", "King"),
    ("Clubs", "4"),
    ("Hearts", "6"),
    ("Hearts", "4"),
    ("Hearts", "7"),
    ("Spades", "9"),
    ("Diamonds", "5"),
    ("Spades", "6"),
    ("Clubs", "Jack"),
    ("Hearts", "Queen"),
    ("Spades", "10"),
]

SORTED_DECK = [
    Card("Diamonds", "2"),
    Card("Diamonds", "3"),
    Card("Diamonds", "4"),
    Card("Diamonds", "5"),
    Card("Diamonds", "6"),
    Card("Diamonds", "7"),
    Card("Diamonds", "8"),
    Card("Diamonds", "9"),
    Card("Diamonds", "10"),
    Card("Diamonds", "Jack"),
    Card("Diamonds", "Queen"),
    Card("Diamonds", "King"),
    Card("Diamonds", "Ace"),
    Card("Spades", "2"),
    Card("Spades", "3"),
    Card("Spades", "4"),
    Card("Spades", "5"),
    Card("Spades", "6"),
    Card("Spades", "7"),
    Card("Spades", "8"),
    Card("Spades", "9"),
    Card("Spades", "10"),
    Card("Spades", "Jack"),
    Card("Spades", "Queen"),
    Card("Spades", "King"),
    Card("Spades", "Ace"),
    Card("Clubs", "2"),
    Card("Clubs", "3"),
    Card("Clubs", "4"),
    Card("Clubs", "5"),
    Card("Clubs", "6"),
    Card("Clubs", "7"),
    Card("Clubs", "8"),
    Card("Clubs", "9"),
    Card("Clubs", "10"),
    Card("Clubs", "Jack"),
    Card("Clubs", "Queen"),
    Card("Clubs", "King"),
    Card("Clubs", "Ace"),
    Card("Hearts", "2"),
    Card("Hearts", "3"),
    Card("Hearts", "4"),
    Card("Hearts", "5"),
    Card("Hearts", "6"),
    Card("Hearts", "7"),
    Card("Hearts", "8"),
    Card("Hearts", "9"),
    Card("Hearts", "10"),
    Card("Hearts", "Jack"),
    Card("Hearts", "Queen"),
    Card("Hearts", "King"),
    Card("Hearts", "Ace"),
]

SORTED_DECK_TUPLES = [
    ("Diamonds", "2"),
    ("Diamonds", "3"),
    ("Diamonds", "4"),
    ("Diamonds", "5"),
    ("Diamonds", "6"),
    ("Diamonds", "7"),
    ("Diamonds", "8"),
    ("Diamonds", "9"),
    ("Diamonds", "10"),
    ("Diamonds", "Jack"),
    ("Diamonds", "Queen"),
    ("Diamonds", "King"),
    ("Diamonds", "Ace"),
    ("Spades", "2"),
    ("Spades", "3"),
    ("Spades", "4"),
    ("Spades", "5"),
    ("Spades", "6"),
    ("Spades", "7"),
    ("Spades", "8"),
    ("Spades", "9"),
    ("Spades", "10"),
    ("Spades", "Jack"),
    ("Spades", "Queen"),
    ("Spades", "King"),
    ("Spades", "Ace"),
    ("Clubs", "2"),
    ("Clubs", "3"),
    ("Clubs", "4"),
    ("Clubs", "5"),
    ("Clubs", "6"),
    ("Clubs", "7"),
    ("Clubs", "8"),
    ("Clubs", "9"),
    ("Clubs", "10"),
    ("Clubs", "Jack"),
    ("Clubs", "Queen"),
    ("Clubs", "King"),
    ("Clubs", "Ace"),
    ("Hearts", "2"),
    ("Hearts", "3"),
    ("Hearts", "4"),
    ("Hearts", "5"),
    ("Hearts", "6"),
    ("Hearts", "7"),
    ("Hearts", "8"),
    ("Hearts", "9"),
    ("Hearts", "10"),
    ("Hearts", "Jack"),
    ("Hearts", "Queen"),
    ("Hearts", "King"),
    ("Hearts", "Ace"),
]

SORT_ORDER = ["Diamonds", "Spades", "Clubs", "Hearts"]

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"

def test_basic_deck_create():
    deck = Deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK


def test_basic_deck_iter():
    deck = Deck(empty=True)
    with pytest.raises(StopIteration):
        card = next(deck)

    deck = Deck()
    for i in range(0, 52):
        card = next(deck)
        assert card == UNSHUFFLED_DECK[i]
    with pytest.raises(StopIteration):
        card = next(deck)

    deck.new_deck()
    for i in range(0, 52):
        card = next(deck)
        assert card == UNSHUFFLED_DECK[i]
    with pytest.raises(StopIteration):
        card = next(deck)

    deck.new_deck()
    for i in range(0, 52):
        assert deck[i] == UNSHUFFLED_DECK[i]


def test_basic_empty_deck():
    deck = Deck(empty=True)
    assert len(deck) == 0
    assert deck == []
    assert deck.top_card is None

    card_1 = Card("Clubs", "9")
    deck.add_card(card_1)
    assert len(deck) == 1
    assert deck == [card_1]
    assert deck.top_card == card_1

    card_2 = Card("Spades", "King")
    deck.add_card(card_2)
    assert len(deck) == 2
    assert deck == [card_1, card_2]
    assert deck.top_card == card_2

    deck.new_deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK
    assert deck.top_card == UNSHUFFLED_DECK[-1]


def test_basic_deck_draw():
    deck = Deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK
    assert deck.top_card == UNSHUFFLED_DECK[-1]

    card = deck.get_card()
    assert len(deck) == 51
    assert card == UNSHUFFLED_DECK[-1]
    assert deck == UNSHUFFLED_DECK[:-1]
    assert deck.top_card == UNSHUFFLED_DECK[-2]

    for i in range(50, -1, -1):
        card = deck.get_card()
        assert card == UNSHUFFLED_DECK[i]
    assert len(deck) == 0
    assert deck == []

    assert deck.top_card is None

    with pytest.raises(DeckEmptyError):
        card = deck.get_card()

    with pytest.raises(DeckEmptyError):
        card = deck.get_card()

    assert len(deck) == 0
    assert deck == []

    deck.new_deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK
    assert deck.top_card == UNSHUFFLED_DECK[-1]


def test_basic_deck_shuffle():
    deck = Deck()
    deck.shuffle()
    assert len(deck) == 52
    assert deck != UNSHUFFLED_DECK
    assert set(deck) == set(UNSHUFFLED_DECK)

    deck.get_card()
    assert len(deck) == 51
    assert deck != UNSHUFFLED_DECK[:-1]
    assert set(deck).issubset(UNSHUFFLED_DECK)

    for i in range(0, 50):
        deck.get_card()
    deck.shuffle()
    assert len(deck) == 1
    assert set(deck).issubset(UNSHUFFLED_DECK)

    deck.get_card()
    deck.shuffle()
    assert len(deck) == 0
    assert deck == []

    with pytest.raises(DeckEmptyError):
        card = deck.get_card()

    assert deck.top_card is None

    deck.shuffle()
    assert len(deck) == 0
    assert deck == []

    deck.new_deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK
    assert deck.top_card == UNSHUFFLED_DECK[-1]


def test_basic_deck_shuffle_seed():
    rand = Random()
    rand.seed(1)
    deck = Deck(random_instance=rand)
    deck.shuffle()
    assert len(deck) == 52
    assert deck == SHUFFLED_DECK_1
    assert deck.top_card == SHUFFLED_DECK_1[-1]

    card = deck.get_card()
    assert len(deck) == 51
    assert card == SHUFFLED_DECK_1[-1]
    assert deck == SHUFFLED_DECK_1[:-1]
    assert deck.top_card == SHUFFLED_DECK_1[-2]

    for i in range(50, -1, -1):
        card = deck.get_card()
        assert card == SHUFFLED_DECK_1[i]
    assert len(deck) == 0
    assert deck == []
    assert deck.top_card is None

    deck.new_deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK
    assert deck.top_card == UNSHUFFLED_DECK[-1]


def test_basic_deck_sort():
    deck = Deck()
    sorted_deck = deck.sort_cards(SORT_ORDER)
    assert len(sorted_deck) == 52
    assert sorted_deck == SORTED_DECK
    assert sorted_deck.top_card == SORTED_DECK[-1]

    card = sorted_deck.get_card()
    assert len(sorted_deck) == 51
    assert card == SORTED_DECK[-1]
    assert sorted_deck == SORTED_DECK[:-1]
    assert sorted_deck.top_card == SORTED_DECK[-2]

    for i in range(50, -1, -1):
        card = sorted_deck.get_card()
        assert card == SORTED_DECK[i]
    assert len(sorted_deck) == 0
    assert sorted_deck == []
    assert sorted_deck.top_card is None

    sorted_deck = sorted_deck.sort_cards(SORT_ORDER)
    assert sorted_deck == []

    deck = Deck()
    card_1 = deck.get_card()
    card_2 = deck.get_card()
    sorted_deck = deck.sort_cards(SORT_ORDER)
    assert sorted_deck == list(filter(lambda x: x not in [card_1, card_2],
                               SORTED_DECK))
    assert sorted_deck.top_card == SORTED_DECK[-1]

    deck = Deck()
    deck.shuffle()
    sorted_deck = deck.sort_cards(SORT_ORDER)
    assert sorted_deck == SORTED_DECK
    assert sorted_deck.top_card == SORTED_DECK[-1]

    deck.new_deck()
    assert len(deck) == 52
    assert deck == UNSHUFFLED_DECK
    assert deck.top_card == UNSHUFFLED_DECK[-1]


def test_basic_deck_string():
    rand = Random()
    rand.seed(1)
    deck = Deck()
    assert str(deck) == str(UNSHUFFLED_DECK_TUPLES)
    deck.get_card()
    assert str(deck) == str(UNSHUFFLED_DECK_TUPLES[:-1])

    deck = Deck(random_instance=rand)
    deck.shuffle()
    assert str(deck) == str(SHUFFLED_DECK_1_TUPLES)
    deck.get_card()
    assert str(deck) == str(SHUFFLED_DECK_1_TUPLES[:-1])

    deck = Deck()
    sorted_deck = deck.sort_cards(SORT_ORDER)
    assert str(sorted_deck) == str(SORTED_DECK_TUPLES)
    sorted_deck.get_card()
    assert str(sorted_deck) == str(SORTED_DECK_TUPLES[:-1])
    for i in range(0, 51):
        sorted_deck.get_card()
    assert str(sorted_deck) == str([])

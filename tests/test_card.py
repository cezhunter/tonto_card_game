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

from card import Card
from exception import InvalidCardRankError, InvalidCardSuitError

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"

def test_basic_card_create():
    card = Card("Spades", "9")
    assert card.rank.name == "9"
    assert card.rank.value == 9
    assert card.suit.name == "Spades"
    assert card.suit.value == 1
    assert card.score == 9

    card = Card("Hearts", "King")
    assert card.rank.name == "King"
    assert card.rank.value == 13
    assert card.suit.name == "Hearts"
    assert card.suit.value == 3
    assert card.score == 39

    card = Card(Card.SUIT.Spades, "9")
    assert card.rank.name == "9"
    assert card.rank.value == 9
    assert card.suit.name == "Spades"
    assert card.suit.value == 1
    assert card.score == 9

    card = Card("Hearts", Card.RANK.King)
    assert card.rank.name == "King"
    assert card.rank.value == 13
    assert card.suit.name == "Hearts"
    assert card.suit.value == 3
    assert card.score == 39


def test_basic_card_null_create():
    with pytest.raises(TypeError):
        card = Card()

    with pytest.raises(TypeError):
        card = Card("Hearts")


def test_basic_card_invalid_attribute():
    with pytest.raises(InvalidCardSuitError):
        card = Card("None", "King")

    with pytest.raises(InvalidCardRankError):
        card = Card("Spades", "None")


def test_basic_card_string():
    card = Card("Spades", "9")
    assert str(card) == "9 of Spades"

    card = Card("Clubs", "Jack")
    assert str(card) == "Jack of Clubs"


def test_basic_card_compare():
    c_1 = Card("Spades", "9")
    c_2 = Card("Clubs", "Jack")
    assert c_1 < c_2
    assert c_2 > c_1

    c_1 = Card("Spades", "9")
    c_2 = Card("Spades", "9")
    assert c_1 == c_2

    c_1 = Card("Spades", "9")
    c_2 = Card("Clubs", "9")
    assert c_1 != c_2

    c_1 = Card("Spades", "9")
    c_2 = Card("Spades", "Jack")
    assert c_1 != c_2

    c_1 = Card("Spades", "9")
    assert c_1 != "9 of Spades"

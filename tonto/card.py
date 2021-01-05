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

"""The fundamental module used to represent cards in a deck or even standalone.

This module allows a user to create a playing card by initiating a Card object
with a suit and rank.

  Example usage:

  card_1 = Card("Clubs", "King")
  card_2 = Card("Hearts", "8")
  card_3 = Card("Diamonds", 7)
"""

from enum import IntEnum
from typing import Union

from exception import InvalidCardRankError, InvalidCardSuitError

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"


class Card:

    """The Card class used to represent playing cards.

    Card object is initiated with both suit and rank. Suit and rank are
    implemented via Integer Enum, allowing access to both name and value. Card
    also keeps track of Score (to be used later in Game and by Players).
    Different instances of Cards can be compared (<, >, or ==). String
    representation is available.

    Attributes:
        rank: An enum representation of the card rank.
        suit: An enum representation of the card suit.
    """

    ALL_RANKS = list(map(str, range(2, 11))) + ["Jack", "Queen", "King", "Ace"]
    RANK = IntEnum("Rank", ALL_RANKS, start=2)  # type: ignore[misc]
    SUIT = IntEnum("Suit", "Spades Diamonds Hearts Clubs")

    def __init__(
        self, suit: Union[str, SUIT], rank: Union[int, str, RANK]
    ) -> None:
        """Initiates Card with a Suit and Rank.

        Args:
            suit: The suit of the playing card.
            rank: The rank of the playing card.

        Raises:
            InvalidCardSuitError: The card suit Suit does not exist.
            InvalidCardRankError: The card rank Rank does not exist.
        """
        try:
            if isinstance(rank, self.RANK):
                self.rank = rank
            else:
                self.rank = getattr(self.RANK, str(rank))
            if isinstance(suit, self.SUIT):
                self.suit = suit
            else:
                self.suit = getattr(self.SUIT, suit)
        except AttributeError as e:
            if suit == str(e):
                raise InvalidCardSuitError(e) from None
            if str(rank) == str(e):
                raise InvalidCardRankError(e) from None

    @property
    def score(self) -> int:
        """Calculates score of Card using int values of rank and suit.

        Returns:
            Card's suit value multiplied by the rank value as score.

        """
        return self.suit.value * self.rank.value

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __str__(self):
        return "{rank} of {suit}".format(rank=self.rank.name,
                                         suit=self.suit.name)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank.value > other.rank.value

    def __lt__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank.value < other.rank.value

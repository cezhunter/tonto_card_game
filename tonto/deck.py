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

"""The module used to create decks of playing cards for a Game or Player hand.

This module allows a user to create a playing card deck by either initiating
an empty deck or an unshuffled one.

  Example usage:

  deck_1 = Deck(empty=True)
  deck_2 = Deck()
  deck_2.shuffle()
  card = deck_2.get_card()
"""

from random import Random
from typing import List, Optional

from tonto.card import Card
from tonto.exception import DeckEmptyError

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"


class Deck:

    """The Deck class to be used to create and manage decks of playing cards.

    Deck objects can be initiated as empty decks using the empty argument or
    as a new unshuffled standard deck. Optionally, an instance of a random
    object can be accepted to determine shuffling. Decks can have cards
    shuffled, added, removed, or have their top cards "turned" (viewed). Decks
    can also be sorted based on a given order of suits. Decks can be compared
    to other decks (==). Decks are iterable.
    """

    def __init__(
        self, empty: bool = False, random_instance: Optional[Random] = None
    ) -> None:
        """Initiates either an empty Deck or an unshuffled standard Deck.

        Args:
            empty: Whether the deck should start out empty.
            random_instance:
                Optional; If given, will use to shuffle instead of internal
                instance.
        """
        self._current_card = 0
        self._deck: List[Card] = []
        self._rand = Random()
        if random_instance:
            self._rand = random_instance
        if not empty:
            self._initiate_deck()

    def add_card(self, card: Card) -> None:
        """Adds Card to the top of the Deck.

        Args:
            card: Whether the deck should start out empty.
        """
        self._deck.append(card)

    def get_card(self) -> Card:
        """Pulls card from the top of the Deck.

        Returns:
            Card from the top of the Deck.

        Raises:
            DeckEmptyError: The deck has run out of cards.
        """
        try:
            return self._deck.pop()
        except IndexError:
            raise DeckEmptyError from None

    def new_deck(self) -> None:
        """Re-initializes back to an unshuffled Deck."""
        self._initiate_deck()

    def shuffle(self) -> None:
        """Shuffles the Deck using an internal instance of Random or the one
        that was passed at initialization of Deck.
        """
        self._rand.shuffle(self._deck)

    def sort_cards(self, order: List[str]) -> "Deck":
        """Sorts Deck based on a given order of Suits.

        Args:
            order: List of Suit strings.

        Returns:
            A new Deck that has been sorted accordingly.
        """
        sorted_deck = Deck(empty=True)
        for suit in order:
            for card in sorted([deck for deck in self._deck
                                if deck.suit.name == suit]):
                sorted_deck.add_card(card)
        return sorted_deck

    @property
    def top_card(self) -> Optional[Card]:
        """Gives the Card on the top of the Deck without removing it.

        Returns:
            The top Card. If nothing is there, None is returned.
        """
        try:
            return self._deck[-1]
        except IndexError:
            return None

    def _initiate_deck(self) -> None:
        """Internal method to initialize a Deck to a standard deck of Cards."""
        self._deck = [Card(suit, rank)
                      for suit in Card.SUIT
                      for rank in Card.RANK]
        self._current_card = 0

    def __bool__(self):
        return bool(self._deck)

    def __getitem__(self, index):
        return self._deck[index]

    def __hash__(self):
        return hash(tuple(self._deck))

    def __iter__(self):
        return iter(self._deck)

    def __len__(self):
        return len(self._deck)

    def __next__(self):
        try:
            card = self._deck[self._current_card]
        except IndexError:
            raise StopIteration from None
        self._current_card += 1
        return card

    def __str__(self):
        tuple_list = [(card.suit.name, card.rank.name) for card in self._deck]
        return str(tuple_list)

    def __eq__(self, other):
        if isinstance(other, Deck):
            return self._deck == other._deck
        if isinstance(other, list):
            return self._deck == other
        return False

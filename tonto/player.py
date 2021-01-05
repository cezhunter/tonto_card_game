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

"""The module used to create a Player or multiple Players for a Game.

The Player class provides the ability to track and manage a person's hand of
playing cards and their score through out a game. The Players class provides
the ability to generate and manage multiple Player instances given a list of
names. The Players class also provides leaderboard metrics.

  Example usage:

  player_1 = Player("Berkelly")
  card_1 = Card("Clubs", "9")
  player_1.draw_card(card_1)
  print(player_1.score())

  players = Players(["Berkelly", "Tonto"])
  card_1 = Card("Hearts", "10")
  players.Berkelly.draw_card(card_1)
  print(players.first().name)
"""

from collections import namedtuple
from typing import Dict, List

from tonto.card import Card
from tonto.deck import Deck
from tonto.exception import InvalidPlayerError

PLACE = namedtuple(
    "Place",
    ["player", "players", "name", "names", "place", "score", "tie"])
EMPTY_PLACE = PLACE(None, [], None, [], 0, 0, False)

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"


class Player:

    """The Player class is used to manage a person's hand and score.

    Player objects are initiated by passing a person's name. Their hand starts
    out as an empty Deck and is expanded by drawing Cards. Player total score
    or score after a specific round can be received. A Player can be compared
    to another Player based on score (< or >) or based on name and hand (==).

    Attributes:
        hand: The Player's hand of playing cards they currently hold.
        name: The Player's name.
    """

    def __init__(self, name: str) -> None:
        """Initiates Player with a name and an empty hand.

        Args:
            name: Name of player.
        """
        self.hand = Deck(empty=True)
        self.name = name

    def clear_hand(self) -> None:
        """Empty the Player's hand."""
        self.hand = Deck(empty=True)

    def draw_card(self, card: Card) -> None:
        """Have the Player draw a card.

        Args:
            card: The Card to add to the Player's hand.
        """
        self.hand.add_card(card)

    def score(self, round_number: int = 0) -> int:
        # We are assuming 1-indexed round numbers
        """Calculate and return the Player's total or round score.

        Args:
            card:
                Optional; The Card to add to the Player's hand.
        """
        if round_number:
            if round_number > len(self.hand):
                return 0
            return self.hand[round_number - 1].score
        return sum([card.score for card in self.hand])

    def __str__(self):
        return "{name} holds {hand} totalling {points} points".format(
            name=self.name, hand=self.hand, points=self.score())

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.hand == other.hand and self.name == other.name

    def __gt__(self, other):
        if not isinstance(other, Player):
            return False
        return self.score() > other.score()

    def __lt__(self, other):
        if not isinstance(other, Player):
            return False
        return self.score() < other.score()


class Players:

    """The Players class is used to create and manage multiple Players.

    Players is initiated by passing a list of names. Each name is then used to
    create a Player and to set an external facing attribute. The main benefit
    of Players is the ability to track score and a leaderboard across multiple
    instances of Player. Players can be printed as a string which translates
    to a game leaderboard. Players can be compared to other Players (==) based
    on list of Player objects. Players are also iterable.

    Attributes:
        PLAYER_NAME: The Player's name can be used to access the corresponding
        Player object.
    """

    def __init__(self, names: List[str]) -> None:
        """Initiates Players by converting given names into Player objects.

        Args:
            names: List of player names.
        """
        self._current_player = 0
        self._players: List[Player] = []
        for name in names:
            if hasattr(self, name):
                raise InvalidPlayerError(name)
            player = Player(name)
            self._players.append(player)
            setattr(self, name, player)

    def reset(self) -> None:
        """Resets the object by clearing the hand of the Players"""
        for player in self._players:
            player.clear_hand()
        self._current_player = 0

    def first(self, round_number: int = 0) -> PLACE:
        """Receives the NamedTuple representation of a Player that has won
        first place in total or only for a given round number.

        Args:
            round_number: Round number.
        """
        return self._get_leaderboard(round_number).get(1, EMPTY_PLACE)

    def second(self, round_number: int = 0) -> PLACE:
        """Receives the NamedTuple representation of a Player that has won
        second place in total or only for a given round number.

        Args:
            round_number: Round number.
        """
        return self._get_leaderboard(round_number).get(2, EMPTY_PLACE)

    def third(self, round_number: int = 0) -> PLACE:
        """Receives the NamedTuple representation of a Player that has won
        third place in total or only for a given round number.

        Args:
            round_number: Round number.
        """
        return self._get_leaderboard(round_number).get(3, EMPTY_PLACE)

    def _get_leaderboard(self, rn: int = 0) -> Dict[int, PLACE]:
        """Produces a dictionary where the keys are a leaderboard position and
        the values are corresponding PLACE namedtuples that are structured as
        such:
            player: First or only Player in position.
            players: All Players in position.
            name: First or only Player name in position.
            names: All Players names in position.
            place: Position.
            score: Score of Player or Players in position.
            tie: If there is a tie for the position (more than 1 Player).

        Args:
            rn: Round number.

        Returns:
            A leaderboard dictionary containing the PLACE namedtuples
            corresponding to the positions on the leaderboard.
        """
        # We sort the list of players based on a total or round score. For
        # every score that repeats itself, we add the correspodning player
        # to a list and keep track of its position in the scoreboard. We
        # generate a namedtuple of information like the players in the list,
        # their names, if its a tie, and the score. This namedtuple is then
        # stored in the dictionary with its corresponding position as the key.
        # This becomes very useful for managing ties in the game.
        l_b = sorted(
            self._players, key=lambda x: x.score(rn), reverse=True)
        l_b_dict = {}
        place = 1
        i = 0
        while i < len(l_b):
            lis = []
            player = l_b[i]
            while i < len(l_b) and player.score(rn) == l_b[i].score(rn):
                lis.append(l_b[i])
                i += 1
            place_nt = PLACE(
                player=lis[0],
                players=lis,
                name=lis[0].name,
                names=[p.name for p in lis],
                place=place,
                score=player.score(rn),
                tie=len(lis) > 1)
            l_b_dict[place] = place_nt
            place += 1
        return l_b_dict

    def __getitem__(self, index):
        return self._players[index]

    def __iter__(self):
        return iter(self._players)

    def __len__(self):
        return len(self._players)

    def __next__(self):
        try:
            player = self._players[self._current_player]
        except IndexError:
            raise StopIteration from None
        self._current_player += 1
        return player

    def __str__(self):
        leaderboard = self._get_leaderboard()
        leaderboard_list = []
        for place, place_nt in leaderboard.items():
            for name in place_nt.names:
                leaderboard_list.append(
                    "{place}: {player} ({score})".format(
                        place=place, player=name, score=place_nt.score))
        return "\n".join(leaderboard_list)

    def __eq__(self, other):
        if isinstance(other, Players):
            return self._players == other._players
        if isinstance(other, list):
            return self._players == other
        return False

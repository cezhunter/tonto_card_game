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

"""The module used to create and play a Game.

Game is used to initiate a card game with some Players by passing a list of
player names. Calling .play() kicks off the game and continues invoking a new
round until the max number of rounds is reached, printing the final scoreboard
after the game ends.

    Example usage:

    game = Game(["Berkelly", "Tonto"])
    game.play()
"""

from typing import Dict, List, Optional
from configparser import ConfigParser
from os.path import abspath, dirname, join
from random import Random
from string import Template

from tonto.deck import Deck
from tonto.exception import GameError, DeckEmptyError
from tonto.player import Players

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"


class Game:

    """The Game class allows users to start new card games.

    Game objects are initiated with a list of the names of the players who
    wish to play. Optionally, a custom message dictionary can be passed for a
    change in game verbiage. A custom Deck can also be used. The max number of
    rounds is 3 by default. A Game can be started using .play() and new rounds
    will be played until the max number of rounds is reached. During each
    round, players take turns drawing cards by pressing enter. After the game
    is finished, a final scoreboard is printed. A new Game can be played after
    invoking .new_game().

    Attributes:
        players: Game's Players object.
    """

    def __init__(
        self,
        names: List[str],
        deck: Optional[Deck] = None,
        max_rounds: int = 3,
        message: Optional[Dict[str, List[str]]] = None
    ) -> None:
        """Initiates a Game by creating Players from names. Creates a Deck and
        shuffles if none is supplied. Generates internal message dictionary
        from messages.conf if none is supplied. Sets max rounds to 3 if none
        is supplied. Sets Game to active.
        Args:
            name: Names of players.
            message:
                Optional; Message dictionary used for game verbiage.
            deck:
                Optional; Deck to use during the game.
            max_rounds:
                Optional; Max number of rounds to play.
        """
        if max_rounds < 1:
            raise GameError("Invalid max number of rounds.")
        if len(names) == 0:
            raise GameError("Invalid number of players.")
        if message:
            self._message = message
        else:
            conf_reader = ConfigParser()
            try:
                message_path = join(dirname(abspath(__file__)),
                                    "messages.conf")
                with open(message_path) as file:
                    conf_reader.read_file(file)
            except IOError:
                raise GameError(
                    "Could not open messages config file.") from None
            self._message = {k: list(v.values())
                             for k, v in dict(conf_reader).items()}
        if deck:
            self._deck = deck
        else:
            self._deck = Deck()
            self._deck.shuffle()
        self.players = Players(names)
        self._current_round = 1
        self._is_active = True
        self._max_rounds = max_rounds
        self._rand = Random()

    def end_game(self) -> None:
        """Sets game to inactive thus ending the Game."""
        self._is_active = False

    def new_game(self) -> None:
        """Resets the Game: Sets Game back to active, resets Players, creates
        new Deck and shuffles.
        """
        self._is_active = True
        self._deck.new_deck()
        self._deck.shuffle()
        self._current_round = 1
        self.players.reset()

    def play(self) -> None:
        """Launches game. Keeps initiating a new round until Game is no longer
        active (max round limit reached). Prints leaderboard at the end.
        """
        self._display_message("WELCOME")
        while self._is_active:
            self._display_message(
                "ROUND START",
                current_round=self._current_round)
            self._next_round()
            last_round = self._current_round - 1
            if self.players.first(last_round).tie:
                self._display_message("ROUND END TIE")
            else:
                self._display_message(
                    "ROUND END",
                    round_winner=self.players.first(last_round).name)
        if self.players.first().tie:
            self._display_message("GAME OVER TIE")
        else:
            self._display_message(
                "GAME OVER",
                game_winner=self.players.first().name)
        print(self.players)

    def _next_round(self) -> None:
        """Starts the next round. Iterates through Players and asks them to
        draw a Card by hitting enter. If the Deck runs out of Cards will
        display a notification and generate a new Deck to draw from.
        """
        for player in self.players:
            self._display_message(
                "TURN START",
                current_player_name=player.name)
            input("Hit enter to draw a card.")
            try:
                card = self._deck.get_card()
            except DeckEmptyError:
                self._display_message("EMPTY DECK")
                self._deck.new_deck()
                self._deck.shuffle()
                card = self._deck.get_card()
            player.draw_card(card)
            pos_result = player in self.players.first().players
            self._display_message(
                "{result} TURN END".format(result=str(pos_result).upper()),
                current_player_name=player.name,
                current_card=card,
                current_player_score=player.score())
        if self._current_round >= self._max_rounds:
            self.end_game()
        self._current_round += 1

    def _display_message(self, category: str, **kwargs) -> None:
        """Takes a category of message and randomly selects a corresponding
        message template from the instance's message dictionary, subsititutes
        any given args, and prints message.

        Args:
            category: Message category.
            **kwargs: Any arguments to be subsituted in the message template
        """
        message = self._rand.choice(self._message[category])
        message_template = Template(message)
        print(message_template.substitute(kwargs))

    def __bool__(self):
        return self._is_active

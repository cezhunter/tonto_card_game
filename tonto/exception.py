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

"""Module for defining Card, Deck, Player, and Game related exceptions.
"""

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"


class DeckEmptyError(Exception):  # pylint: disable=missing-class-docstring

    def __init__(self):
        self.message = "The deck has run out of cards."
        super().__init__(self.message)


class GameError(Exception):  # pylint: disable=missing-class-docstring

    def __init__(self, err):
        self.message = "Not a valid game: {err}".format(
            err=err)
        super().__init__(self.message)


class InvalidCardError(Exception):  # pylint: disable=missing-class-docstring

    def __init__(self, err):
        self.message = "{err} is not a valid card.".format(
            err=err)
        super().__init__(self.message)


class InvalidCardRankError(Exception):  # pylint: disable=missing-class-docstring

    def __init__(self, err):
        self.message = "The card rank '{err}' does not exist.".format(
            err=err)
        super().__init__(self.message)


class InvalidCardSuitError(Exception):  # pylint: disable=missing-class-docstring

    def __init__(self, err):
        self.message = "The card suit '{err}' does not exist.".format(
            err=err)
        super().__init__(self.message)


class InvalidPlayerError(Exception):  # pylint: disable=missing-class-docstring

    def __init__(self, err):
        self.message = "{err} is not a valid player.".format(
            err=err)
        super().__init__(self.message)

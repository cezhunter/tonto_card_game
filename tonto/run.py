#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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

"""Entry point for Tonto's Card Game to be played via CLI. Takes as aguments a
list of names and (optional) a max number of rounds. Asks player(s) if they
would like to play again after each game."""

import argparse

from tonto.game import Game

__author__ = "Cezanne Vahid"
__copyright__ = "Copyright 2020, Tonto's Card Game"
__credits__ = ["Cezanne Vahid", "Tonto Gonzalez"]
__email__ = "cezannevahid@gmail.com"
__license__ = "MIT"
__maintainer__ = "Cezanne Vahid"
__status__ = "Production"
__version__ = "1.0.0"

def main():
    parser = argparse.ArgumentParser(description="Play Tonto's Card Game!")
    parser.add_argument(
        "names", type=str, nargs="+",
        help="Names of players who wish to play.")
    parser.add_argument(
        "--rounds", type=int, default=3, help="Maximum number of rounds.")
    args = parser.parse_args()

    game = Game(args.names, max_rounds=args.rounds)
    agree_to_play = True
    while agree_to_play:
        game.play()
        no_valid_response = True
        while no_valid_response:
            response = input("Play again? (Y/N)")
            if response.lower() in ["y", "n", "yes", "no"]:
                no_valid_response = False
            else:
                print("Not a valid response.")
        if response.lower() in ["n", "no"]:
            agree_to_play = False
        game.new_game()


def entry():
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nGoodbye.")


if __name__ == "__main__":
    entry()

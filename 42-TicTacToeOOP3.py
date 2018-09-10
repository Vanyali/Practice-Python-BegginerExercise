#! /usr/bin/env python3
#
#    tictactoe - A simple tic-tac-toe game
#
#    (C) 2017 - Richard Neumann <mail at richard dash neumann dot de>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""A simple Tic-Tac-Toe game"""

from itertools import chain


class InvalidInput(Exception):
    """Indicates an invalid user input"""

    def __init__(self, message):
        """Sets the message to the user"""
        super().__init__(message)
        self.message = message


class FieldIsOccupied(Exception):
    """Indicates that the selected field is occupied"""

    pass


class GameEnd(Exception):
    """Indicates the end of the game"""

    def __init__(self, winner):
        """Sets the respective winner"""
        super().__init__(winner)
        self.winner = winner


class Player():
    """Player and field values"""

    CROSS = 'x'
    CIRCLE = 'o'
    NONE = ' '


class TicTacToe():
    """The game class"""

    def __init__(self):
        """Initializes field and last player"""
        self.field = [[Player.NONE] * 3, [Player.NONE] * 3, [Player.NONE] * 3]
        self.last_player = Player.NONE

    def __str__(self):
        """Converts the game field into a string"""
        return '{}║{}║{}\n═╬═╬═\n{}║{}║{}\n═╬═╬═\n{}║{}║{}'.format(
            *chain(*self.field))

    @property
    def win_patterns(self):
        """Yields patterns significant for winning"""
        # Rows
        yield self.field[0]
        yield self.field[1]
        yield self.field[2]
        # Columns
        yield (self.field[0][0], self.field[1][0], self.field[2][0])
        yield (self.field[0][1], self.field[1][1], self.field[2][1])
        yield (self.field[0][2], self.field[1][2], self.field[2][2])
        # Diagonals
        yield (self.field[0][0], self.field[1][1], self.field[2][2])
        yield (self.field[0][2], self.field[1][1], self.field[2][0])

    @property
    def next_player(self):
        """Returns the next player"""
        if self.last_player is Player.CROSS:
            return Player.CIRCLE

        return Player.CROSS

    def check_winner(self):
        """Check if the game has ended"""
        draw = True

        for fields in self.win_patterns:
            if fields[0] in (Player.CROSS, Player.CIRCLE):
                if all(fields[0] == field for field in fields[1:]):
                    raise GameEnd(fields[0])
            elif any(field is Player.NONE for field in fields):
                draw = False

        if draw:
            raise GameEnd(Player.NONE)

    def make_turn(self, player, column, row):
        """Makes a turn"""
        if self.field[row][column] is Player.NONE:
            self.last_player = self.field[row][column] = player
        else:
            raise FieldIsOccupied()

    @property
    def player_input(self):
        """Reads input from player"""
        coords = input('Turn for {}: '.format(self.next_player))

        try:
            column, row = coords.split()
        except ValueError:
            raise InvalidInput('Please enter: "<column> <row>"')
        else:
            try:
                column, row = int(column), int(row)
            except ValueError:
                raise InvalidInput('Coordinates must be integers.')
            else:
                if all(0 <= i <= 2 for i in (column, row)):
                    return column, row

                raise InvalidInput('Coordinates must be 0 <= i <=2.')

    def start(self):
        """Starts the game"""
        while True:
            print(self)

            try:
                self.check_winner()
            except GameEnd as game_end:
                if game_end.winner is Player.CROSS:
                    print('Cross wins.')
                elif game_end.winner is Player.CIRCLE:
                    print('Circle wins.')
                else:
                    print('The game ended in a draw.')

                break

            try:
                column, row = self.player_input
            except KeyboardInterrupt:
                print('\nGame aborted.')
                return False
            except InvalidInput as invalid_input:
                print(invalid_input.message)
            else:
                try:
                    self.make_turn(self.next_player, column, row)
                except FieldIsOccupied:
                    print('The selected field is occupied.')

        try:
            input('Press enter to exit...')
        except KeyboardInterrupt:
            print()


def main():
    """Runs a new game"""

    game = TicTacToe()
    game.start()


if __name__ == '__main__':
    main()
import click

from cards import Cards
from board import Board

@click.command()
@click.argument("num_players")
def main(num_players):
    print("Clue: Not you Miss White, not you")
    print("Let's use {} players".format(num_players))

    cards = Cards()

    board = Board()

    players = Players()

if "__main__" == __name__:
    main()
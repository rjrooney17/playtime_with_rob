import click
import logging
import Tkinter as tk

from board import Board
from player import Player

@click.command()
@click.argument("num_players")
def main(num_players):
    logging.basicConfig(level=logging.INFO)
    logging.info("Let's play clue with {} players".format(num_players))

    root = tk.Tk()
    root.title("Clue!!!")
    root.geometry('{}x{}'.format(350, 550))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    board = Board(root)

    for pn in Player.PLAYER_CONFIGURATIONS.keys():
        p = Player(pn, board.frame)
        board.add_player(p)

    tk.mainloop()

if "__main__" == __name__:
    main()
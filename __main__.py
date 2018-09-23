import click
import Tkinter as tk

from board import Board

@click.command()
@click.argument("num_players")
def main(num_players):
    print("Let's play clue with {} players".format(num_players))

    root = tk.Tk()
    root.title("Clue!!!")
    root.geometry('{}x{}'.format(350, 550))
    board = Board(root)
    tk.mainloop()

if "__main__" == __name__:
    main()
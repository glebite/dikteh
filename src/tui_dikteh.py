"""tui_dikteh.py
"""
import sys
import pandas as pd
import string
from speech import Speaker
import curses
from cli_dikteh import CLI


class TUI(CLI):
    """TUI 
    """
    def __init__(self, wordfile, sentence_count):
        super(TUI, self).__init__(wordfile , sentence_count)
        self.stdscr = None
        pass

    def start_display(self):
        """start_display - instantiate the screen member
        """
        self.stdscr = curses.initscr()

    def stop_display(self):
        """stop_display - shut down the display for now
        """
        self.stdscr.endwin()

    def __del__(self):
        """__del__ - handle the destruction of the object
        """
        self.stop_display()


if __name__ == "__main__":
    x = TUI(sys.argv[1], sys.argv[2])
    x.load_sentences()
    x.game_play()


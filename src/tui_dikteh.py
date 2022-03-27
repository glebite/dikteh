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
        """
        """
        self.stdscr = curses.initscr()

    def stop_display(self):
        """
        """
        self.stdscr.endwin()

    def __del__(self):
        """
        """
        pass


if __name__ == "__main__":
    x = TUI(sys.argv[1], sys.argv[2])
    x.load_sentences()
    x.game_play()


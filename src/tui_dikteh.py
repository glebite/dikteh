"""tui-dikteh.py
"""
import sys
import pandas as pd
import string
from speech import Speaker
import curses
from cli-dikteh import CLI


class TUI(CLI):
    """TUI 
    """
    def __init__(self, wordfile, sentence_count):
        self.stdscr = None
        pass

    def config(self):
        """
        """
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
    pass

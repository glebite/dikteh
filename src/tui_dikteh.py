"""tui_dikteh.py
"""
import sys
import pandas as pd
import string
from speech import Speaker
import curses
from cli_dikteh import CLI
import time


class TUI(CLI):
    """TUI 
    """
    def __init__(self, wordfile, sentence_count):
        super(TUI, self).__init__(wordfile , sentence_count)
        self.stdscr = None

    def start_display(self):
        """start_display - instantiate the screen member
        """
        self.stdscr = curses.initscr()
        if not self.stdscr:
            print("Problem opening the window...")
        curses.noecho()
        curses.curs_set(0)

    def stop_display(self):
        """stop_display - shut down the display for now
        """
        curses.curs_set(1)
        self.stdscr.endwin()

    def label(self, row, column, message):
        """
        """
        self.stdscr.addstr(row, column, message)
        self.stdscr.refresh()

    def display_stats(self):
        """
        """
        pass
        
    def __del__(self):
        """__del__ - handle the destruction of the object
        """
        self.stop_display()

    """ interaction code """
    
    def game_play(self):
        """
        """
        self.start_display()
        self.display_progress()
        time.sleep(10)
        self.stop_display()
    
    def accept_input(self):
        """
        """
        pass

    def display_progress(self):
        """
        """
        self.label(1,2, 'Sentence 1/4')
        self.label(2,3, 'Success: 5')

    def create_report(self):
        """
        """
        pass


if __name__ == "__main__":
    x = TUI(sys.argv[1], sys.argv[2])
    x.load_sentences()
    x.game_play()

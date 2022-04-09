"""tui_dikteh.py
"""
import sys
import curses
import curses.textpad
import time
from cli_dikteh import CLI


TITLE_COORDS = (0,0)
SEN_COUNT_COORDS = (5,60)
SUCCESS_COORDS = (6,60)
MISSED_COORDS = (7,60)


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
        curses.endwin()

    def label(self, row_col, message):
        """
        """
        row, column = row_col
        self.stdscr.addstr(row, column, message)
        self.stdscr.refresh()

    def text_input(self, row_col, width_height):
        """text_input - text box
        """
        row, column = row_col
        width, height = width_height
        self.stdscr.addstr(row-1, column, 'User Input:')
        self.outwin = self.stdscr.subwin(3 ,30, row, column)
        self.outwin.immedok(True)
        self.outwin.box()
        tb = curses.textpad.Textbox(self.outwin, insert_mode=True)
        self.outwin.addstr(1, 1, 'whatever')
        self.stdscr.refresh()

    def last_response(self, row_col):
        row, column = row_col
        self.stdscr.addstr(row-1, column, 'Game message:')
        self.outwin = self.stdscr.subwin(3 ,30, row, column)
        self.outwin.immedok(True)
        self.outwin.box()
        tb = curses.textpad.Textbox(self.outwin, insert_mode=True)
        self.outwin.addstr(1, 1, 'Misspelled: wrangler')
        self.stdscr.refresh()        
        
    def __del__(self):
        """__del__ - handle the destruction of the object
        """
        # self.stop_display()

    def display_progress(self):
        """
        """
        self.label(TITLE_COORDS, 'TUI-Dikteh go for 20!')
        self.label(SEN_COUNT_COORDS, f'Sentence 1/{self.sentences_to_play}')
        self.label(SUCCESS_COORDS,  f'Success: {self.score["success"]}')
        self.label(MISSED_COORDS, f'Missed : {self.score["missed"]}')        

    """ interaction code """
    
    def game_play(self):
        """
        """
        self.start_display()
        self.display_progress()
        self.text_input((5,10), (5,5))
        self.last_response((10,10))
        time.sleep(10)
        self.stop_display()
    
    def create_report(self):
        """
        """
        pass


if __name__ == "__main__":
    x = TUI(sys.argv[1], sys.argv[2])
    x.load_sentences()
    x.game_play()

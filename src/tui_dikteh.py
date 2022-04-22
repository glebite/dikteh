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
TEXT_INPUT_COORDS = (5,5)
EXPECTED_COORDS = (10, 5)
YOUR_COORDS = (15,5)
LAST_RESPONSE_SIZE = (3, 50)

class TUI(CLI):
    """TUI 
    """
    def __init__(self, wordfile, sentence_count):
        super(TUI, self).__init__(wordfile , sentence_count)

    def start_display(self):
        """start_display - instantiate the screen member
        """
        self.stdscr = curses.initscr()
        self.last_message = ""
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
        """label - draws text at a specified row, column point
        """
        row, column = row_col
        self.stdscr.addstr(row, column, message)
        self.stdscr.refresh()

    def user_input(self, row, col):
        curses.echo()
        self.stdscr.refresh()
        self.stdscr.addstr(row + 1, col +1, " " * 36)
        input = self.stdscr.getstr(row + 1, col + 1, 40)
        return input
    
    def text_input(self, row_col, width_height):
        """text_input - text box
        """
        row, column = row_col
        width, height = width_height
        self.stdscr.addstr(row-1, column, 'User Input:')
        self.outwin = self.stdscr.subwin(3 ,40, row, column)
        self.outwin.immedok(True)
        self.outwin.border(0)

        self.last_message = self.user_input(row, column).decode('ascii').strip()

        self.stdscr.refresh()

    def last_response(self, row_col, title, word):
        """last_response - feedback provided for the last response
        """
        row, column = row_col
        height, width = LAST_RESPONSE_SIZE
        self.stdscr.addstr(row-1, column, title)
        self.outwin = self.stdscr.subwin(height, width, row, column)
        self.outwin.immedok(True)
        self.outwin.box()
        self.outwin.addstr(1, 1, " " * 36)
        self.outwin.addstr(1, 1, word)
        self.stdscr.refresh()        
        
    def __del__(self):
        """__del__ - handle the destruction of the object
        """
        # self.stop_display()

    def display_progress(self):
        """ display_progress
        """
        self.label(TITLE_COORDS, 'TUI-Dikteh go for 20!')
        self.label(SEN_COUNT_COORDS, f'Sentence 1/{self.sentences_to_play}')
        self.label(SUCCESS_COORDS,  f'Success: {self.score["success"]}')
        self.label(MISSED_COORDS, f'Missed : {self.score["missed"]}')        

    """ interaction code """
    def game_play(self):
        """ game_play
        """
        result = list()
        self.start_display()
        self.display_progress()
        x = self.pick_random_sentence()
        sentence = self.remove_punctuation(x).split()
        for word in sentence:
            word = word.lower()
            self.speaker.speak(word)
            self.text_input(TEXT_INPUT_COORDS, (5,5))
            self.last_response(EXPECTED_COORDS, 'Expected word:', word)
            self.last_response(YOUR_COORDS, 'Your word:', self.last_message)
            result.append((word, self.last_message))            
            if word != self.last_message:
                self.score['missed'] += 1
            else:
                self.score['success'] += 1
            self.display_progress()
             
        self.stop_display()

    def create_report(self):
        """ create_report
        """
        pass


if __name__ == "__main__":
    x = TUI(sys.argv[1], sys.argv[2])
    x.load_sentences()
    x.game_play()

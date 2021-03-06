"""tui_dikteh.py
"""
import sys
import curses
import curses.textpad
import configparser
import random
from missed_handler import MissedWords
from cli_dikteh import CLI


TITLE_COORDS = (0,0)
SEN_COUNT_COORDS = (5,60)
SUCCESS_COORDS = (6,60)
MISSED_COORDS = (7,60)
TEXT_INPUT_COORDS = (5,5)
EXPECTED_COORDS = (10, 5)
YOUR_COORDS = (15,5)
LAST_RESPONSE_SIZE = (3, 50)
NEW_SENTENCE_COORDS = (3,5)
LAST_SENTENCE_COORDS = (20,5)
LAST_SENTENCE_SIZE = (3, 60)


class TUI(CLI):
    """TUI - text UI class

    This text UI uses curses - handy indeed for terminals.
    """
    def __init__(self, wordfile, sentence_count):
        super(TUI, self).__init__(wordfile , sentence_count)
        self.current_sentence = 1
        self.missed_words = MissedWords('missed_words.json')
        self.missed_words.read_words()

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
        """user_input - handle a user input region
        
        params:
        row - int - the row (y) to draw the segment
        col - int - the column (x) to draw the segment

        returns:
        user_input - string - contains what the user typed
        """
        curses.echo()
        self.stdscr.refresh()
        self.stdscr.addstr(row + 1, col +1, " " * 36)
        user_input = self.stdscr.getstr(row + 1, col + 1, 40)
        return user_input
    
    def text_input(self, row_col, width_height):
        """text_input - text box
        
        params:
        row_col - tuple - the row and column of the box
        width_height - tuple - width and height

        return:
        n/a

        raises:
        n/a
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
        pass

    def display_progress(self):
        """ display_progress
        """
        self.label(TITLE_COORDS, 'TUI-Dikteh go for 20!')
        self.label(SEN_COUNT_COORDS, f'Sentence {self.current_sentence}/{self.sentences_to_play}')
        self.label(SUCCESS_COORDS,  f'Success: {self.score["success"]}')
        self.label(MISSED_COORDS, f'Missed : {self.score["missed"]}')        

    def pick_previously_failed_word(self):
        """
        Pick a word that had been previously failed.  But only
        if there are failed words.  :)
        """
        return_val = None
        if len(self.missed_words.missed_words):
            return_val = random.choice(list(self.missed_words.missed_words))
        return return_val

    def display_last_sentence(self, title, words):
        row, column = LAST_SENTENCE_COORDS
        height, width = LAST_SENTENCE_SIZE
        self.stdscr.addstr(row-1, column, title)
        self.outwin = curses.newpad(height, width)
        self.outwin.scrollok(1)
        self.outwin.immedok(True)
        self.outwin.box()
        self.outwin.addstr(1, 1, " " * (width-2))
        self.outwin.addstr(1, 1, words)
        self.stdscr.refresh()        

    """ interaction code """
    def game_play(self):
        """ game_play
        """
        result = list()
        self.start_display()
        self.display_progress()
        pickword = self.pick_previously_failed_word()
        
        for round in range(self.sentences_to_play):
            self.label(NEW_SENTENCE_COORDS, 'New Sentence')
            x = self.pick_random_sentence(bias=pickword)
            pickword = None
            sentence = self.remove_punctuation(x).split()
            for word in sentence:
                word = self.remove_punctuation(word).lower().replace("???", "'")
                self.speaker.speak(word)
                self.text_input(TEXT_INPUT_COORDS, (5,5))
                self.last_response(EXPECTED_COORDS, 'Expected word:', word)
                self.last_response(YOUR_COORDS, 'Your word:', self.last_message)
                result.append((word, self.last_message))            
                if word != self.last_message:
                    self.score['missed'] += 1
                    self.missed_words.add_word(word)
                else:
                    self.score['success'] += 1
                    self.missed_words.del_word(word)
                self.display_progress()
                self.label(NEW_SENTENCE_COORDS, '            ')
            self.display_last_sentence('Last Sentence:', str(x))
            self.current_sentence += 1
            self.display_progress()
        self.stop_display()

    def create_report(self):
        """ create_report
        """
        print('Writing out missed words for this session:')
        self.missed_words.write_words()
        for missed_word in self.missed_words.missed_words.keys():
            print(f'Missed: {missed_word}')


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    sentences = config['Dikteh']['SentenceFile']
    num_plays = config['Dikteh']['NumberOfSentences']
    x = TUI(sentences, num_plays)
    x.load_sentences()
    x.game_play()
    x.create_report()

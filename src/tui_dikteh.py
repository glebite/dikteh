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

        self.last_message = self.user_input(row, column)

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
    # def game_play(self):
    #     """game_play - play the loop

    #     params:
    #     n/a

    #     returns:
    #     n/a

    #     raises:
    #     n/a
    #     """
    #     for count in range(1, self.sentences_to_play+1):
    #         print(f'Playing sentence {count} of {self.sentences_to_play}.')
    #         sentence = self.pick_random_sentence().tolist()[0].split()
    #         for word in sentence:
    #             word = self.remove_punctuation(word).lower().replace("’", "'")
    #             self.speaker.speak(word)
    #             readword = input('Enter the word that you heard: ')
    #             readword = readword.strip()
    #             if readword != word:
    #                 print(
    #                     f'You typed: {readword} word spoken was: {word}')
    #                 self.score['missed'] += 1
    #                 self.failed_words.append((word, readword))
    #             else:
    #                 self.score['success'] += 1
    #                 print(f'Correct!')
    #         print(f'\nThe sentence was: {sentence}')
    #     self.report_score()
        
    def game_play(self):
        """ game_play
        """
        self.start_display()
        self.display_progress()
        x = self.pick_random_sentence()
        sentence = x.tolist()[0].split()
        for word in sentence:
            self.speaker.speak(word)
            self.text_input(TEXT_INPUT_COORDS, (5,5))
            self.last_response(EXPECTED_COORDS, 'Expected word:', word)
            self.last_response(YOUR_COORDS, 'Your word:', self.last_message)
            if word != self.last_message:
                self.score['missed'] += 1
            else:
                self.score['success'] += 1
            self.display_progress()
             
        time.sleep(10)
        self.stop_display()
        print(x)
    
    def create_report(self):
        """ create_report
        """
        pass


if __name__ == "__main__":
    x = TUI(sys.argv[1], sys.argv[2])
    x.load_sentences()
    x.game_play()

"""
"""
import sys
import pandas as pd
import string
from speech import Speaker


class CLI:
    """
    """
    def __init__(self, wordfile):
        """
        """
        self.wordfile = wordfile
        self.speaker = Speaker()
        self.speaker.configure()
        pd.set_option('display.max_colwidth', None)

    def load_sentences(self):
        """
        """
        self.df = pd.read_excel(self.wordfile)

    def pick_random_sentence(self):
        """
        """
        return self.df.sample()['Sentence'].values

def remove_punctuation(value):
    """
    """
    for character in string.punctuation:
        value = value.replace(character, '')
        return value


if __name__ == "__main__":
    game = CLI(sys.argv[1])
    game.load_sentences()
    for word in game.pick_random_sentence().tolist()[0].split():        
        word = remove_punctuation(word)
        game.speaker.speak(word)
        readword = input('Enter the word that you heard: ')
        if readword != word:
            print(f'You typed: {readword}  and the word spoken was: {word}')
        else:
            print(f'Correct!')

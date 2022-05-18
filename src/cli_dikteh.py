"""cli_dikteh.py
"""
import sys
import pandas as pd
import string
from speech import Speaker


class CLI:
    """CLI - a class to handle this simple game
    """
    def __init__(self, wordfile, sentence_count):
        """
        """
        self.wordfile = wordfile
        self.speaker = Speaker()
        self.speaker.configure()
        self.sentences_to_play = int(sentence_count)
        self.failed_words = list()
        self.score = {'success': 0, 'missed': 0}

        pd.set_option('display.max_colwidth', None)

    def load_sentences(self):
        """load_sentences - load a spreadsheet with the sentences
        """
        self.df = pd.read_excel(self.wordfile)

    def pick_random_sentence(self, bias=None):
        """pick_random_sentence - pick a random one

        params:
        bias - string - a failed word to use

        returns:
        a sample from the list of sentences by value

        raises:
        n/a
        """
        if bias:
            for sentence in self.df['Sentence'].values:
                if bias in sentence:
                    return sentence
        return self.df.sample()['Sentence'].values

    def remove_punctuation(self, sentence):
        """remove_punctuation - just get rid of them all!

        Essentially take the sentence and split it into characters
        while removing any punctuation.

        params:
        sentence - string - the sentence being evaluated

        returns:
        sentence - string - free of punctuation

        raises:
        n/a
        """
        return "".join([char for char in sentence
                        if char not in string.punctuation])

    def report_score(self):
        """report_score - a simple dump of stats, sentences, etc...
        """
        print('\n\nGood work with studying!')
        print(f'Sentences used: {self.sentences_to_play}')
        print(f'Success: {self.score["success"]}')
        print(f'Missed : {self.score["missed"]}')
        print(f'Specifically missed words: ')
        for word, readword in self.failed_words:
            print(f'Expected: {word} Typed: {readword}')

    def game_play(self):
        """game_play - play the loop

        params:
        n/a

        returns:
        n/a

        raises:
        n/a
        """
        for count in range(1, self.sentences_to_play+1):
            print(f'Playing sentence {count} of {self.sentences_to_play}.')
            sentence = self.pick_random_sentence().tolist()[0].split()
            for word in sentence:
                word = self.remove_punctuation(word).lower().replace("’", "'")
                self.speaker.speak(word)
                readword = input('Enter the word that you heard: ')
                readword = readword.strip()
                if readword != word:
                    print(
                        f'You typed: {readword} word spoken was: {word}')
                    self.score['missed'] += 1
                    self.failed_words.append((word, readword))
                else:
                    self.score['success'] += 1
                    print(f'Correct!')
            print(f'\nThe sentence was: {sentence}')
        self.report_score()


if __name__ == "__main__":
    game = CLI(sys.argv[1], sys.argv[2])
    game.load_sentences()
    game.game_play()

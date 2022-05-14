"""missed_handler.py

The premise is that the missed words can be stored
to some file to later be used in further execution
to prioritize the failed words and affect future 
sentence selection.

I think for now, the sentences will pick one random 
word and then use it for swaying the sentence selection
to reinforce learning.  It's cheap.

The other portion of this system is the missed counter 
needing to count up or down based on success during 
game play.

This could be stored as a .json file to make life easier
as much as I dislike json files.

{'words': [{'thesaurus': 3},
{'dictionary': 3}]}

The value of 3 indicates that the player needs to spell
it correctly 3 times now before it can be deemed as part
of the player's lexicon.

If the count goes to zero, the word is removed from the 
missed word file.

If the word is still mispelled, the value is incremented by
1.

Eventually, they will hear "thesaurus" and spell it correctly.
"""
import json
import os


class MissedWords:
    """MissedWords
    """
    def __init__(self, file_name = None):
        """__init__
        """
        if not file_name:
            raise ValueError(f'{file_name=} needs to be not NULL')
        self.missed_file = file_name
        self.missed_words = dict()

    def read_words(self):
        """read_words
        """
        if os.path.isfile(self.missed_file):
            with open(self.missed_file, 'r') as fp:
                temp = fp.read()
                self.missed_words = json.loads(temp)

    def write_words(self):
        """write_words 
        """
        with open(self.missed_file, 'w') as fp:
            fp.write(json.dumps(self.missed_words))

    def add_word(self, word):
        """add_word

        The logic here is that an existing missed_word
        which is missed again gets its counter score
        to increment by one.

        A missed_word doesn't exist in the list of missed
        words, it gets a default value of 3.
        """
        if word in self.missed_words.keys():
            self.missed_words[word] += 1
        else:
            self.missed_words[word] = 3

    def del_word(self, word):
        """del_world

        If the missed word counter is one, we delete
        the missing word from the storage.

        Otherwise, we just knock off the counter by 1.
        """
        if word in self.missed_words.keys():
            if self.missed_words[word] == 1:
                del self.missed_words[word]
            else:
                self.missed_words[word] -= 1

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


class MissedWords:
    """MissedWords
    """
    def __init__(self, word_set=None):
        pass

    def read_words(self):
        pass

    def write_words(self):
        pass
    
if __name__ == "__main__":
    pass

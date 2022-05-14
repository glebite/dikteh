import pytest
from missed_handler import MissedWords


def test_instantiate_object():
    x = MissedWords(file_name='tempword.json')
    if not x:
        assert False, "Should have been able to instantiate"


def test_confirm_initial_empty():
    x = MissedWords(file_name='tempword.json')
    assert len(x.missed_words) == 0


def test_missing_file():
    x = MissedWords(file_name='thisdoesnotexist.json')
    try:
        x.read_words()
        assert False
    except Exception as e:
        assert True, f'Expected exception raised: {e=}'
    
def test_empty_file():
    x = MissedWords(file_name='empty.json')
    try:
        x.read_words()
        assert False
    except Exception as e:
        assert True, f'Expected exception raised: {e=}'        

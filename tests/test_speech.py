import pytest
from speech import Speaker

def test_object_creation():
    x = Speaker()
    assert x, 'Speaker did not get created.'

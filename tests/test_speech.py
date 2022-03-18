import pytest
from speech import Speaker
import functions
from mock import Mock
import sys

class TestA:
    def test_01(self, mocker, capsys):
        sys.modules['platform.system'] = Mock()
        x = Speaker()
        x.configure()
        print(f'Platform? {x.platform=}')

"""
speech.py - the basis of all good things.

"""
import platform
import os


class Speaker:
    """
    """
    def __init__(self):
        """__init__ - constructor for the Speaker class
        """
        pass

    def configure(self):
        self.platform = platform.system()
        if self.platform == 'Windows':
            import win32com.client
            self.speaker = win32com.client.Dispatch('SAPI.SpVoice')
            self.speaker_function = self._winspeak
        elif self.platform == 'Linux':
            import distutils.spawn
            import os
            if not distutils.spawn.find_executable('espeak'):
                raise RuntimeError('espeak not found - install it.')
            self.speaker_function = self._linspeak
        else:
            raise ValueError(f'Unkown os: {self.platform=}')

    def _winspeak(self, message):
        """
        """
        self.speaker.Speak(message)

    def _linspeak(self, message):
        os.system(f'espeak "{message}"')

    def speak(self, message):
        """speak - use the os type to "say" something
        """
        self.speaker_function.__call__(message)


if __name__ == "__main__":
    pass

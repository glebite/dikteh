"""
speech.py - the 

"""
import platform


class Speaker:
    """
    """
    def __init__(self):
        """__init__ - constructor for the Speaker class
        """
        self.platform = platform.system()
        if self.platform == 'Windows':
            import win32com.client
            self.speaker = win32com.client.Dispatch('SAPI.SpVoice')

    def _winspeak(self, message):
        """
        """
        self.speaker.Speak(message)
        
    def speak(self, message):
        """speak - use the os type to "say" something
        """
        pass

    def speak(self, message):
        """
        """
        pass


if __name__ == "__main__":
    pass

"""
<<<<<<< HEAD
speech.py - the 

"""
import platform
=======
"""
>>>>>>> 7549c05332f34db919f41102209020759a521153


class Speaker:
    """
    """
    def __init__(self):
<<<<<<< HEAD
        """__init__ - constructor for the Speaker class
        """
        self.platform = platform.system()
        if self.platform == 'Windows':
            import win32com
            self.speaker = win32com.client.Dispatch('SAPI.SpVoice')

    def _winspeak(self, message):
        """
        """
        self.speaker.Speak(message)
        
    def speak(self, message):
        """speak - use the os type to "say" something
        """
=======
        """
        """
        pass

    def speak(self, message):
        """
        """
        pass
>>>>>>> 7549c05332f34db919f41102209020759a521153


if __name__ == "__main__":
    pass

from .models import Data 

class Logic():
    @classmethod
    def add_file(cls, text, image):
        data = Data(text=text, photo=image)
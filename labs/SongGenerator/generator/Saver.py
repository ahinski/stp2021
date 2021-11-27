import os
from typing import Text
class Saver:
    """A class that represents song saver.
   
        ...
        
        Attributes
        ----------
        text: str
            song text
        path : str
            path to save song
        name: str
            name of created song
        
        Methods
        -------
        song_names()
            Returns song names (names of files in dir) in list.
        song_lines()
            Returns all lines from songs in list.    
    """
    def __init__(self, text, path, name):
        if os.path.isdir(path):
            self.path = path
        else:
            raise ValueError('Provided path is not a directory.')
        self.text = text
        self.name = name

    def save(self):
        """Saves a new song to a specified dir
        """
        with open(self.path + '/' + name, "w+") as file:
            file.write(self.text)
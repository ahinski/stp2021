import os

class Crawler:
    """A class that represents the directory with songs.
    
        ...
        
        Attributes
        ----------
        path : str
            a path to a folder with songs in txt format.
            
        Methods
        -------
        song_names()
            Returns song names (names of files in dir) in list.
        song_lines()
            Returns all lines from songs in list.
    """
    def __init__(self, path):
        if os.path.isdir(path):
            self.path = path
        else:
            raise ValueError('Provided path is not a directory.')
        self.__song_names = os.listdir(self.path)
        
    @property
    def song_names(self):
        return self.__song_names
    
    def song_lines(self):
        lines = []
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".txt"):
                with open(filename) as file:
                    lines_file = file.readlines()
                    lines.append(lines_file.rstrip() for line in lines)
        return lines
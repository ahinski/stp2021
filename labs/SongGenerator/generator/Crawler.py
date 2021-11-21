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
        self.__file_names = os.listdir(self.path)
        
    def song_names(self):
        song_names = []
        for song_name in self.__file_names:
            song_names.append(song_name[:-3])
        return song_names
    
    def song_lines(self):
        lines = []
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".txt"):
                with open(self.path + '\\' + filename, encoding = 'utf-8', mode='r') as file:
                    lines_file = file.readlines()
                    lines += lines_file
        lines = [line + '\n' if line[-1:] != '\n' else line for line in lines]
        lines.remove('\n')
        lines = list(set(lines))
        return lines

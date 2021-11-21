import random
class Generator:
    """A class that represents random-song-generator.
   
        ...
        
        Attributes
        ----------
        lines : str
            lines used to create new song
        
        Methods
        -------
        song_names()
            Returns song names (names of files in dir) in list.
        song_lines()
            Returns all lines from songs in list.    
    """
    def __init__(self, lines):
        self.lines = lines
        
    def generate_song(self, n_lines_verses, n_lines_chorus):
        """Generates a new song from old lines with given parameters.

        Args
        ----
        n_lines_verse : list
            list of number of lines the verse consists of for each verse 
        n_lines_chorus : int
            number of lines the chorus consist of
            
        Returns
        -------
        str: text of new song
        """
        if len(n_lines_verses) < 2:
            raise ValueError('Minimum number of verses should is 2.')
        chorus = self.__verse(n_lines_chorus)
        text = ''
        for n_lines_verse in n_lines_verses:
            text += self.__verse(n_lines_verse)
            text += '\n'
            text += chorus
            text += '\n'
        return text          
            
    def __verse(self, n_lines):
        """Generate verse with given number of lines

        Args:
        -----
        n_lines : int 
            number of lines in a verse
            
        Returns
        -------
        str: text of generated verse
        """
        verse_text = ''
        for n in n_lines:
            random_number = random.randint(0,len(self.lines))
            verse_text += self.lines[random_number]
            self.lines.remove(self.lines[random_number])
        return verse_text
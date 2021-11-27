import time

from generator.Crawler import Crawler
from generator.Generator import Generator
from generator.Saver import Saver

crawler = Crawler('C:\git_projects\stp2021\labs\SongGenerator\songs')
song_generator = Generator(crawler.song_lines())
n_verses = input('Введите кол-во куплетов: ')

n_lines_verse = []
for i in range(int(n_verses)):
    n_lines_verse_tmp = int(input('Введите кол-во строк в ' + str(i+1) + ' куплете: '))
    n_lines_verse.append(n_lines_verse_tmp)
n_lines_chorus = int(input('Введите кол-во строк в припеве: '))

song_text = song_generator.generate_song(n_lines_verse, n_lines_chorus)
print(song_text)
song_name = input('Введите название песни: ')

new_song = Saver(song_text, r'C:\git_projects\stp2021\labs\SongGenerator\new songs', song_name)
new_song.save()
print('Saved!')

time.sleep(5)
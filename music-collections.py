# Задача №2 "Аудиоколлекция"
# Необходимо уметь хранить информацию по альбомам и трекам в них.
# Это можно сделать, используя классы Album и Track.

# У класса Track есть поля:
#
# Название;
# Длительность в минутах(используется тип данных int).
# И метод show, выводящий информацию по
# треку в виде <Название-Длительность>.

# У класса Album есть поля:
#
# Название альбома
# Группа
# Список треков
#
# И три метода:

# get_tracks - выводит информацию по всем трекам(используется метод show).
# add_track - добавление нового трека в список треков.
# get_duration - выводит длительность всего альбома.

# Задание:
# Создать 2 альбома с 3 треками. Для каждого вывести его длительность.

class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        return f'<{self.name} - {self.duration}>'

    def set_name(self, name):
        self.name = name

    def set_duration(self, duration):
        self.duration = duration


class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        return [track.show() for track in self.tracks]

    def get_duration(self):
        return sum([track.duration for track in self.tracks])

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.tracks.append(track)


albums = []
album = Album('The Fat of the Land', 'The Prodigy')
album.add_track(Track('Narayan', 9))
album.add_track(Track('Climbatize', 6))
album.add_track(Track('Breathe', 5))
breakpoint()
albums.append(album)
breakpoint()
album = Album('Опиум', 'Агата Кристи')
album.add_track(Track('Сказочная тайга', 2))
album.add_track(Track('Чёрная луна', 4))
album.add_track(Track('Трансильвания', 4))
albums.append(album)

for album in albums:
    print(f'Альбом "{album.name}" группы {album.group}:')
    for track in enumerate(album.get_tracks(), 1):
        print(f'{track[0]}. {track[1]}')
    print(f'Общая длительность альбома: {album.get_duration()} минут\n')

breakpoint()
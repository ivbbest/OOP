# Задача №2 "Аудиоколлекция". Продолжение.
# В первой части задания вы создали 2 альбома с 3 треками и вывели длительность для каждого.
# Попробуйте получить более подробную информацию о них, опираясь на примеры использования методов в описании заданий:
#
# Задание 1:
# Вместо метода show использовать магический метод __str__ у трека для вывода информации по треку.
# Пример использования
#
# print(track1)
# Bohemian rhapsody-6min
# У Класса Альбом также реализовать магический метод __str__ для вывода информации по альбому и его треков.
#
# Пример использования
#
# print(my_album)
# Name group: Queen
# Name album: Bohemian rhapsody
# Tracks:
# 	Bohemian rhapsody-6min
# 	The show must go on-4min
# Задание 2:
# Реализовать возможность сравнивать треки по длительности. Для этого нужно будет определить магические методы. Пример
#
# track1 = Track('Bohemian rhapsody', 6)
# track2 = Track('The show must go on', 4)
# track1 > track2
# True


class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name}-{self.duration}min'

    def set_name(self, name):
        self.name = name

    def set_duration(self, duration):
        self.duration = duration


class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def __str__(self):
        pass
    

    def get_tracks(self):
        return [str(track) for track in self.tracks]

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

albums.append(album)

album = Album('Опиум', 'Агата Кристи')
album.add_track(Track('Сказочная тайга', 2))
album.add_track(Track('Чёрная луна', 4))
album.add_track(Track('Трансильвания', 4))
albums.append(album)

for album in albums:
    print(f'Name group: {album.group}\nName album: {album.name}')
    for track in enumerate(album.get_tracks(), 1):
        print(f'{track[0]}. {track[1]}')
    print(f'Общая длительность альбома: {album.get_duration()} минут\n')

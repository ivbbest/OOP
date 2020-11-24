# Задача №2 "Аудиоколлекция"
# Необходимо уметь хранить информацию по альбомам и трекам в них.
# Это можно сделать, используя классы Album и Track.

# У класса Track есть поля:
#
# Название;
# Длительность в минутах(используется тип данных int). И метод show, выводящий информацию по
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
    def __init__(self, name_track, minutes):
        self.name_track = name_track
        self.minutes = minutes

    def show(self):
        print(f'<{self.name_track}> - {self.minutes}')


class Album(Track):
    def __init__(self, name_album, name_group):
        self.name_album = name_album
        self.name_group = name_group
        self.list_track = dict()

    def get_tracks(self):
        print(self.list_track)

    def add_track(self, track, minute):
        self.list_track[track] = minute

    def get_duration(self):
        return sum(list(self.list_track.values()))


if __name__ == '__main__':
    topchik = Album('Leto', 'Maksim')
    topchik.add_track('Kak tak', 3)
    topchik.add_track('Moe vremy', 2)
    topchik.add_track('I love', 4)

    topchik.get_tracks()

    duration = topchik.get_duration()
    print(duration)

    breakpoint()
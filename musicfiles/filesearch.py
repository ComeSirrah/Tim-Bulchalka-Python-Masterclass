import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        # caps_name = artist_name.upper()
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in fnmatch.filter(directories, artist_name):

            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):   # we want the path, not the name of the album
            yield song


album_list = find_albums("/media/sirrah/mediabackup/alterholt.backup/Music",
                         "trevor*")
song_list = find_songs(album_list)

# for a in album_list:
#     print(a)

for s in song_list:
    print(s)

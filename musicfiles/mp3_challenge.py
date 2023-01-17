import fnmatch
import id3reader_p3 as id3reader
import os


def music_filepath(root, extension='mp3'):
    for path, directories, files in os.walk(root):
        for song in fnmatch.filter(files, f'*.{extension}'):
            absfilepath = os.path.abspath(path)
            yield os.path.join(absfilepath, song)


root1 = "/media/sirrah/mediabackup/alterholt.backup/Music"

error_files = []

for s in music_filepath(root1, 'mp3'):
    try:
        id3r = id3reader.Reader(s)
        print(f"Artists: {id3r.get_value('performer')}, Album: {id3r.get_value('album')}, "
              f"Track: {id3r.get_value('track')}, Song: {id3r.get_value('title')}")
    except Exception:
        print("ERROR: Data does not seem to work with id3reader module. Are you sure it's mp3?")
        error_files.append(s)
if error_files:
    print(f"\n\n\n{'*' * 80}\nError files include:\n{'*' * 80}")
    for f in error_files:
        print(f)

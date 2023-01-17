import os

root = "/media/sirrah/mediabackup/alterholt.backup/Music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f.split(' - ')
            print(song_details)
        print("*" * 40)

#
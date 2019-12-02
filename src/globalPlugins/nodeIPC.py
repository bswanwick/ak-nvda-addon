import os


def letZamokKnow(message):
    filename = "ZamokNVDA.dat"
    directory = os.getenv('LOCALAPPDATA')
    path = directory + "\\" + filename
    file_object = open(path, "w")
    file_object.write(message)
    file_object.close()
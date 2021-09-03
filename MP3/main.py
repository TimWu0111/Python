import sys
from mp3copy import *
from mp3download import*

def prompt():
    print("[dl] [song_title] [song_url] (Downlaod)")
    print("[ck] [mp3_path] [file_path] (Check)")

def download(title,url):
    song_title = title
    song_url = url

    Download().download_song(song_url, song_title)

def check(mp3, file):
    check = Check()

    mp3_path = mp3
    file_path = file

    namelist = check.mp3file(mp3_path)
    mp3list = check.getname(namelist)
    print(mp3list)
    lostlist = check.compare_dir(mp3list, file_path)
    print(lostlist)

    newlist = check.getlostname(mp3_path, lostlist)
    print(newlist)

    if newlist != "":
        for one in newlist:
            check.copyfile(mp3_path, file_path, one)

if __name__ == "__main__":

    prompt()

    while(True):
        command = input("Use command:\n")
        parameter = command.split(" ")

        #dl Rockabye https://www.youtube.com/watch?v=2VDdP7lYiiI&ab_channel=7clouds
        if parameter[0] == "dl":
            download(parameter[1],parameter[2])

        #ck D:/mp3 D:/test
        elif parameter[0] == "ck":
    	    check(parameter[1],parameter[2])

        elif parameter[0] == "end":
            break

        else:
            prompt()
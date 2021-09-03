from __future__ import unicode_literals
import youtube_dl


class Download():
    @staticmethod
    def download_song(song_url, song_title):

        ydl_opts = {
            'outtmpl': song_title + '.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],

        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
       # url = "https://www.youtube.com/watch?v=2VDdP7lYiiI&ab_channel=7clouds"
       #Rockabye - Clean Bandit ft. Sean Paul & Anne-Marie
            ydl.download([song_url])

# if __name__ == "__main__":
#     #if (len(sys.argv) !=3):
#         #print(sys.argv[0], ": takes 2 arguments, not ", len(sys.argv) - 1, ".")
#
#     song_title = (sys.argv[1])
#     song_url = (sys.argv[2])
#
#     download_song(song_url, song_title)



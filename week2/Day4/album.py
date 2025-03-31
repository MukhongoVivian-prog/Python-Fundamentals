from song import Song
class Album():
    def __init__(self, name):
        self.name = name
        self.songs = []

    def addSong(self,title,artist,release_date, genre):
        song = Song(title,artist,release_date,genre,0)
        self.songs.append(song)

    def showSong(self):
        for song in self.songs:

            print("## Song Name ##: ", song.name)

    def likeSong(self):
        for song in self.songs:
            if Song.title == song.title:
                song.like_song()
                break

album = Album("Dabel's first album")
album.addSong("Unavailable", "Davido","26-03-03","AfroBeat")

print(album.name)
print(album.songs)

album.showSong()

"""
we are building a music streaming website
users can upload songs to the website
users can like songs
users can add sogs to the playlist and uplod albums

***Steps***
Album
-title
-songs(list of songs)

Playlist:
-name
-songs(list of songs)
-like count

Song:
-title
-artist
release date
genre
like count


"""

class Song():
    def __init__(self, name, artist, release_date, genre, likes):
        self.name = name
        self.artist = artist
        self.release_date = release_date
        self.genre = genre
        self.likes = likes

        def like_song(self):
            self.likes += 1 # add the number of likes to the songs

        def unlike_song(self):
            self.likes -= 1   # remove the number of likes to the songs

# =================================================================
# creating he actual song

"""song1 = Song("Unavalable", "Davido","26-03-03","AfroBeat",0)
song2 = Song("Kesse", "Wizzkid","02-03-2024","AfroBeat",0)

print(song1.name)
print(song2.name)"""
from lyricsgenius import Genius

def generate_lyrics(artist: str, name: str):
    token = 'JHzJF-MxqDcKQ0IgQE8v0XKPX7BolD05AmT6Eiv2Y64ruLvObI2O4x7BxG3eLU4k'
    genius = Genius(token)

    song = genius.search_song(name, artist)
    index = song.lyrics.find('Lyrics') + 6
    lyrics = song.lyrics[index:-5]

    return lyrics.replace('\n', ' ')

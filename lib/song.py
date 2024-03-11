class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    test = ''

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_genre(genre)
        self.add_artists(artist)
        self.add_genre_count(genre)
        self.add_artist_count(artist)

        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_genre(cls, genre):
        # if genre not in self.genres:
        #     Song.genres.append(genre)
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count.update({genre: 1})

    @classmethod
    def add_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count.update({artist: 1})


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
no_problems = Song("Jesus be King", "T-kat", "Rap")
fire = Song("Provide Fire", "Tasha Cobbs", "Gospel")
fill_me = Song("Fill me Up", "Tasha Cobbs", "Gospel")


print(fill_me.artist_count)

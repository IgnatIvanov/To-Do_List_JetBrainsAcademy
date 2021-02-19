def tracklist(**tracks):
    for artist in tracks:
        print(artist)
        for album, song in tracks[artist].items():
            print("ALBUM: " + album + " TRACK: " + song)

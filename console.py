from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

import repositories.albums_repo as albums_repo
import repositories.artists_repo as art_repo


albums_repo.delete_all()
art_repo.delete_all()

artist1 = Artist('Dave')
art_repo.add_artist(artist1)
artist2 = Artist('Panos')
art_repo.add_artist(artist2)
artist3 = Artist('Helen')
art_repo.add_artist(artist3)

album1 = Album("Black Roses", "Rock", artist1)
albums_repo.add_album(album1)
album2 = Album("Bloody Love", "Pop", artist3)
albums_repo.add_album(album2)
album3 = Album("Angels from Sky", "Rock", artist1)
albums_repo.add_album(album3)
album4 = Album("Axaristi", "Laika", artist2)
albums_repo.add_album(album4)
album5 = Album("La Luna", "Latin", artist3)
albums_repo.add_album(album5)

artist3.name = "Helena"
art_repo.update(artist3)
album3.artist = artist3
albums_repo.update(album3)
all_artists = art_repo.all_artists()
for artist in all_artists:
    print(artist.__dict__)
all_albums = albums_repo.all_albums()
for album in all_albums:
    
    print(album.__dict__)
all_artist_albums = albums_repo.all_albums_by_artist(artist3)
for album in all_artist_albums:
    print(album.__dict__)

# print(art_repo.single_artist(17))
# print(albums_repo.single_album(19))



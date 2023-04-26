from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artists_repo as art_repo

def add_album(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    album.id = run_sql(sql, values)[0]['id']
    return album

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

def all_albums():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = art_repo.single_artist(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def all_albums_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    for row in results:
        artist = art_repo.single_artist(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def single_album(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results:
        artist = art_repo.single_artist(results['artist_id'])
        album = Album(results['title'], results['genre'], artist, results['id'])
    return album

def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)
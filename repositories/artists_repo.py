from   db.run_sql import run_sql
from  models.artist import Artist


def add_artist(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    artist.id  = run_sql(sql, values)[0]['id']
    return artist

def update(artist):
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


def all_artists():
    artists = []
    sql_str = "SELECT * FROM artists"
    results = run_sql(sql_str)

    for row in results:
        artist = Artist(row['name'],row['id'])
        artists.append(artist)
    
    return artists

def single_artist(id):
    artist = None
    sql_str = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql_str, values)

    if results:
        artist = Artist(results[0]['name'], results[0]['id'])
    return artist


def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

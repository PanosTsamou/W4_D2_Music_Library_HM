import psycopg2
import psycopg2.extras as ext

def run_sql(sql_str, values = None):
    conn = None
    results = []
    try:
        conn = psycopg2.connect(dbname = 'music_collection')
        cur = conn.cursor(cursor_factory= ext.DictCursor)
        cur.execute(sql_str, values)
        conn.commit()
        
        results = cur.fetchall()
        cur.close
    except (Exception, psycopg2.DatabaseError) as error:
        print("Something went WRONG!!!", error)
    finally:
        if conn is not None:
            conn.close()

    return results
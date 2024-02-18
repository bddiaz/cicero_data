import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def addPlayer():
    sql ="""INSERT INTO players (id, nba_api_id, updated_at, name, team, position)
            VALUES (1,2, '2024-02-18','LeBron James','LAL', 'everything')"""
    config = load_config()
    try:
        
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT command
                cur.execute(sql)
                rows = cur.fetchone()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    addPlayer()



import psycopg2


def insert_data(table_name: str, args: list) -> None:

    with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as con:
        with con.cursor() as cur:

            count = ''.join('%s,' * len(args[0]))
            query = f"INSERT INTO {table_name} VALUES ({count[:-1]})"

            cur.executemany(query, args)

    con.close()

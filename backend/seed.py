from database import get_connection, create_tables

connection = get_connection()

connection.execute("DROP TABLE IF EXIST items")
connection.commit()
connection.close()

create_tables()


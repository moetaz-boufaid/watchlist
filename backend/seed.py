from database import get_connection, create_table


connection = get_connection()
connection.execute("DROP TABLE IF EXISTS items")
connection.commit()
connection.close()

create_table()

items = [
    ("Hollow Knight", "game", 10, "Amazing world"),
    ("Inception", "movie", 9, "Great ending"),
    ("Berserk", "book", 10, "Dark but incredible"),
]
connection = get_connection()
for item in items:
    connection.execute(
        "INSERT INTO items (title, type, rating, note) VALUES(?,?,?,?)",
        item,
    )
connection.commit()
connection.close()

print('done' , len(items), 'items added')
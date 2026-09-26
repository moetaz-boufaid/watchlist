from flask import Flask, render_template
from database import get_connection, create_table

app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")
create_table()

@app.route("/")
def home():
    connection = get_connection()
    items = connection.execute("SELECT * FROM items").fetchall()
    connection.close()
    return render_template("index.html", items=items)

@app.route("/games")
def game():
    connection = get_connection()
    items = connection.execute("SELECT * FROM  items WHERE type='game'").fetchall()
    connection.close()
    return render_template("category.html", items=items,category="Games")

@app.route("/movies")
def movie():
    connection = get_connection()
    items = connection.execute("SELECT * FROM   items WHERE type = 'movie'").fetchall()
    connection.close()
    return render_template("category.html", items=items,category="movies")

@app.route("/books")
def books():
    connection = get_connection()
    items = connection.execute("SELECT * FROM   items WHERE type = 'book'").fetchall()
    connection.close()
    return render_template("category.html", items=items,category="books")


app.run(debug=True)
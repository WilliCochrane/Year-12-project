# Made my me 30/04/2024
from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/about')
def aboutpage():
    return "about"


@app.route('/route/<int:id>')
def route(id):
    conn = sqlite3.connect('climbing.db')
    cur = conn.cursor()
    cur.execute("SELECT name,stars,climbing_type_id,grade,length,bolts,rock_wall_id FROM Route WHERE id = '{}'".format(id))
    route = cur.fetchall()
    print(route)
    return render_template('route.html', name=route[0][0], )


if __name__ == "__main__":  # Last lines
    app.run(debug=True)

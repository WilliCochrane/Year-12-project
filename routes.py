# Made my me 30/04/2024
from flask import Flask, render_template
import sqlite3


app = Flask(__name__, static_url_path='/static')


def do_sql(sql):
    conn = sqlite3.connect('climbing.db')
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def num_to_stars(num:int):
    if num == 0:
        stars = "/static/Icons/no-star.png"
    elif num == 1:
        stars = "/static/Icons/one-star.png"
    elif num == 2:
        stars = "/static/Icons/two-star.png"
    elif num == 3:
        stars = "/static/Icons/three-star.png"
    else:
        stars = "/static/Icons/no-star.png"
    return stars


@app.route('/')
def homepage():
    return render_template('route.html')


@app.route('/about')
def aboutpage():
    return "about"


@app.route('/route/<int:id>')
def route(id):
    route = do_sql("SELECT name,stars,climbing_type_id,grade,length,bolts,rock_wall_id FROM Route WHERE id = '{}'".format(id))
    print(route)
    stars = num_to_stars(route[0][1])
    return render_template('route.html', name=route[0][0], stars=stars, climbing_type_id=route[0][2], grade=route[0][3], length=route[0][4], bolts=route[0][5], rock_wall_id=route[0][6])

if __name__ == "__main__":  # Last lines
    app.run(debug=True)

from flask import Flask, redirect, render_template, request, url_for
import sqlite3
from sql_query.get_band_sql import getBandSql


def get_db_connection():
    conn = sqlite3.connect("./db/metal-repo.db")
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)

band_array = []


@app.route("/")
def index():
    conn = get_db_connection()
    bands = conn.execute(getBandSql.get_sql).fetchall()
    conn.close()

    return render_template("index.html", bands=bands)


@app.route("/add", methods=["POST"])
def add_band():
    band_name = request.form.get("band_name")
    if band_name:
        band_array.append(band_name)

    return redirect(url_for("index"))

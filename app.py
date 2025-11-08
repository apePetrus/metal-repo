from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

band_array = []


@app.route("/")
def index():
    return render_template("index.html", bands=band_array)


@app.route("/add", methods=["POST"])
def add_band():
    band_name = request.form.get("band_name")
    if band_name:
        band_array.append(band_name)

    return redirect(url_for("index"))
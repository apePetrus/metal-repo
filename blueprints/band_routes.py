from flask import Blueprint, redirect, render_template, request, url_for
from classes.band.band import Band

band_bp = Blueprint("band", __name__)


@band_bp.route("/")
def index():
    bands = Band().getBands()

    return render_template("index.html", bands=bands)


@band_bp.route("/add", methods=["POST"])
def add_band():
    band_array = []

    band_name = request.form.get("band_name")
    if band_name:
        band_array.append(band_name)

    return redirect(url_for("band.index"))

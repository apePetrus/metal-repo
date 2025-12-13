from flask import Flask
from blueprints.band_routes import band_bp


app = Flask(__name__)

app.register_blueprint(band_bp)

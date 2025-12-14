from flask import Flask
from blueprints.band_routes import band_bp
from repositories.init_db import init_db

init_db()
app = Flask(__name__)

app.register_blueprint(band_bp)

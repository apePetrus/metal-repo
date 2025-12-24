from flask import Flask
from blueprints.band_routes import band_bp
from repositories.init_db import init_db
from data.seeder import Seeder

init_db()
app = Flask(__name__)

Seeder().yaml_test()

app.register_blueprint(band_bp)

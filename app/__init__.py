from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config

# make app
app = Flask(__name__)
app.config.from_object(config.Config())

# init db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import app, db, routes
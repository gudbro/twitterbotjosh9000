import sqlite3
from os import getenv
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
# ----------------------------------- Flask ---------------------------------- #
app = Flask(__name__)
host = getenv('HOST')
port = getenv('PORT')
# --------------------------------- DB Config -------------------------------- #
app.config['SQLALCHEMY_DATABASE_URI'] = false  #getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false #getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)
# ---------------------------------------------------------------------------- #
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ---------------------------------------------------------------------------- #
class Status(db.Model):
    __tablename__ = 'message-ids'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.CharField, max_length=280, unique=True)


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    manager.run()
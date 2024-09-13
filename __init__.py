from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1357@192.168.29.144:5432/counter_inc_db"
db = SQLAlchemy(app)



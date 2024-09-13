# create_tables.py
from app import app, db

with app.app_context():
    db.create_all()
# with app.app_context():
#     db.drop_all()
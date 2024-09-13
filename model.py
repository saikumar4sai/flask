from __init__ import app, db
# from . import app, db


class Counter(db.Model):
    __tablename__ = "Counter"
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer, default=0)
    b = db.Column(db.Integer, default=0)
    c = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<id{self.id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

with app.app_context():
    db.create_all()

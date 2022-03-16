from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    score = db.Column(db.Integer(0, 10), unique=False, nullable=False)
    title = db.Column(db.String(100), unique=True, nullable=False)
    review = db.Column(db.String(250), unique=True, nullable=True)

    def _repr_(self):
        return "<Score %r>" % self.score

# Add any model classes for Flask-SQLAlchemy here
from . import db


class AddMovie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200))
    poster=db.Column(db.String(),nullable=True)
    created_at=db.Column(db.DateTime(80))
    


def __init__(self,title,description,poster,created_at):
        
        self.title= title
        self.description =description
        self.poster = poster
        self.created_at= created_at

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def get_id(self):
    try:
         return unicode(self.id)  # python 2 support
    except NameError:
        return str(self.id)  # python 3 support

def __repr__(self):
    return '<AddMovie "{}">'.format(self.id)
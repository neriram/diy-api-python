from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/catsql'
db = SQLAlchemy(app)

class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "age": self.age
        }
        
    def __repr__(self):
        return f'Cat(id={self.id}, name="{self.name}", type="{self.type}", age={self.age})'
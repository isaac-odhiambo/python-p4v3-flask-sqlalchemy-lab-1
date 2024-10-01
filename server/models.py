from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    magnitude = db.Column(db.Float)  # Float for earthquake magnitude
    location = db.Column(db.String)  # String for location
    year = db.Column(db.Integer)  # Integer for the year of the earthquake

    def __repr__(self):
        return f'{self.id}, {self.magnitude}, {self.location}, {self.year}'
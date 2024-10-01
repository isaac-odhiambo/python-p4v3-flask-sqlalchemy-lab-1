# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    session = db.session  # Use the session from the db instance
    earthquake = session.get(Earthquake, id)  # Use Session.get() to fetch the earthquake

    if earthquake is None:
        return jsonify({"message": f"Earthquake {id} not found."}), 404  # Include the ID in the error message

    # Create a dictionary with the earthquake details
    earthquake_data = {
        "id": earthquake.id,
        "location": earthquake.location,
        "magnitude": earthquake.magnitude,
        "year": earthquake.year
    }
    
    return jsonify(earthquake_data)  # Return the earthquake data as JSON

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    # Query the database for earthquakes with magnitude greater than or equal to the parameter
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    # Create a list of earthquake data
    earthquake_data = [
        {
            "id": eq.id,
            "location": eq.location,
            "magnitude": eq.magnitude,
            "year": eq.year
        }
        for eq in earthquakes
    ]
    
    # Return the count of matching rows and the list of data under the correct key
    return jsonify({"count": len(earthquake_data), "quakes": earthquake_data})  # Changed "earthquakes" to "quakes"
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)

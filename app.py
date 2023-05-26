from flask import Flask
from flask_pymongo import PyMongo
import os

# Create an instance of the Flask class
app = Flask(__name__)

# Configure MongoDB connection
username = os.environ.get('username')
password = os.environ.get('password')
database = 'footskill'
cluster_url = 'footskillcluster.t2szqp3.mongodb.net'

app.config['MONGO_URI'] = f'mongodb+srv://{username}:{password}@{cluster_url}/{database}?retryWrites=true&w=majority'

# Create an instance of PyMongo
mongo = PyMongo(app)

# Define a route and its corresponding handler function
@app.route('/')
def index():
    # Access MongoDB collection
    collection = mongo.db.players

    # Perform database operations
    data = collection.find()

    return 'Hello, World!' + username

@app.route('/players/<player_name>')
def get_player(player_name):
    # Access the "players" collection
    collection = mongo.db.players

    # Find the document with the specified player_name
    player = collection.find_one({"name": player_name})

    # Check if the player exists
    if player:
        # Return the player details as JSON response
        return jsonify(player)
    else:
        # Return an error message if player is not found
        return jsonify({'error': 'Player not found'}), 404

@app.route('/players')
def listPlayers():
    # Access MongoDB collection
    collection = mongo.db.players

    # Perform database operations
    data = collection.find()

    # result = "Players:<br/>"
    # for d in data:
    #     result += d.name + '<br/>'

    return data
 

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run()

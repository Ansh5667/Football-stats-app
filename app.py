from flask import Flask, render_template, request, Flask
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['football_stats']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teams')
def teams():
    # Retrieve teams from the database and render the teams page template
    tm = db['statistics'].find()
    return render_template('teams.html', teams=tm)


@app.route('/players')
def player_profile():
    # Fetch player information from the database using player_id
    player = db.players.find()

    return render_template('pp.html', players=player)


if __name__ == '__main__':
    app.run(debug=True)



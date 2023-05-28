from dataclasses import dataclass #funciones
from flask import Flask, jsonify,  request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@dataclass
class Player(db.Model):
    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    

    def _repr_(self):
        return f'<Player {self.username}>'
    
    def check_password(self, password):
        return self.password == password
    
with app.app_context():
    db.create_all()

@app.route('/players', methods=['GET','POST'])
def route_get_players():
    if request.method == 'GET':
        return get_players()
    elif request.method == 'POST':
        json_data = request.json
        return insert_player(json_data)

@app.route('/players/<player_id>', methods=['GET','PUT']) #PUT=Update
def route_get_player(player_id):
    if request.method == 'GET':
        return get_player_by_id(player_id)
    elif request.method == 'PUT':
        player = request.get_json()
        return update_player(player_id, player)

@app.route('/players/add',  methods = ['POST'])
def route_add_player():
    player = request.get_json()
    return insert_player(player)

@app.route('/players/update',  methods = ['PUT'])
def route_update_player():
    player = request.get_json()
    return update_player(player)

@app.route('/players/delete/<player_id>',  methods = ['GET', 'DELETE'])
def route_delete_player(player_id):
    return delete_player(player_id)

def get_players():
    players = Player.query.all()
    return players

def insert_player(json_data):
    player = Player(username=json_data['username'], password=json_data['password'])
    db.session.add(player)
    db.session.commit()
    return 'SUCCESS'

def get_player_by_id(player_id):
    player = Player.query.filter_by(id = player_id).first() 
    return jsonify(player)

def update_player(player_id, player_nuevo):
    player = Player.query.get(player_id)
    if player : 
        player.username = player_nuevo.get('username')
        player.password = player_nuevo.get('password')
        db.session.commit()
        return 'SUCCESS'

def delete_player(player_id):
    player=Player.query.get(player_id)
    db.session.delete(player)
    db.session.commit()
    return 'SUCCESS'

@app.route('/list')
def route_adress():
    return render_template('list.html')   
    
@app.route('/list_js')
def route_listjs():
    return render_template('list.js')  




if __name__ == '__main__':
    app.run()

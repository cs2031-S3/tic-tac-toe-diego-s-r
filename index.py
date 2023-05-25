from dataclasses import dataclass
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
    

    def __repr__(self):
        return f'<Player {self.username}>'
    
    def check_password(self, password):
        return self.password == password
    
with app.app_context():
    db.create_all()

#CRUD
@app.route('/players', methods=['GET','POST'])
def route_get_players():
    if request.method == 'GET':
        return get_players()
    elif request.method == 'POST':
        json_data = request.json
        return insert_player(json_data)

@app.route('/players/<player_id>', methods=['GET'])
def route_get_player(player_id):
    return get_player_by_id(player_id)

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


#html y js 
@app.route('/menu_script')
def menu():
    return render_template('menu.html')


@app.route('/list')
def list_menu():
    return render_template('list.html')

@app.route('/list_js')
def list_js():
    return render_template('list.js')


def get_players():
    players = Player.query.all()
    return jsonify(players)

def get_player_by_id(player_id):
    player = Player.query.filter_by(id=player_id).first()
    return jsonify(player)

def insert_player(data):
    player = Player(username=data["username"], password=data["password"])
    db.session.add(player)
    db.session.commit()
    return jsonify(player)

def update_player(player):
    found_player = Player.query.get(player.get('id'))
    if found_player:
        found_player.username = player.get('username')
        found_player.password = player.get('password')
        db.session.commit()
        return jsonify(found_player)
    else:
        return jsonify({'error':'player not found'})


def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    return "SUCCESS"

if __name__ == '__main__':
    app.run()

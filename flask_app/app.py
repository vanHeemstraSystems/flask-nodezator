from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import yaml
from nodezator import Nodezator

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/threagile_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    node_type = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, ForeignKey('node.id'))
    children = relationship("Node")

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_node', methods=['POST'])
def add_node():
    data = request.json
    new_node = Node(name=data['name'], node_type=data['node_type'], parent_id=data.get('parent_id'))
    db.session.add(new_node)
    db.session.commit()
    return jsonify({'id': new_node.id})

@app.route('/export_yaml', methods=['GET'])
def export_yaml():
    nodes = Node.query.all()
    node_dict = {node.id: {'name': node.name, 'type': node.node_type, 'children': []} for node in nodes}
    
    for node in nodes:
        if node.parent_id:
            node_dict[node.parent_id]['children'].append(node.id)

    yaml_data = yaml.dump(node_dict)
    return jsonify({'yaml': yaml_data})

@app.route('/nodes', methods=['GET'])
def get_nodes():
    nodes = Node.query.all()
    return jsonify([{ 'id': node.id, 'name': node.name, 'type': node.node_type, 'parent_id': node.parent_id } for node in nodes])

nodezator = Nodezator(app, db, Node)

if __name__ == '__main__':
    app.run(debug=True)


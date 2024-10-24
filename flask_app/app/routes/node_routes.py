from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.node import Node
from app.forms.node_form import NodeForm
from app.extensions import db

node_bp = Blueprint('node', __name__)

@node_bp.route('/', methods=['GET'])
def list_nodes():
    nodes = Node.query.all()
    return jsonify([{ 'id': node.id, 'name': node.name, 'type': node.node_type, 'parent_id': node.parent_id } for node in nodes])

@node_bp.route('/new', methods=['POST'])
def new():
    data = request.json
    new_node = Node(name=data['name'], node_type=data['node_type'], parent_id=data.get('parent_id'))
    db.session.add(new_node)
    db.session.commit()
    return jsonify({'id': new_node.id})
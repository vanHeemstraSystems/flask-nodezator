import yaml
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models.node import Node
from app.extensions import db

yaml_bp = Blueprint('yaml', __name__)

@yaml_bp.route('/export', methods=['GET'])
def export():
    nodes = Node.query.all()
    node_dict = {node.id: {'name': node.name, 'type': node.node_type, 'children': []} for node in nodes}
    
    for node in nodes:
        if node.parent_id:
            node_dict[node.parent_id]['children'].append(node.id)

    yaml_data = yaml.dump(node_dict)
    return jsonify({'yaml': yaml_data})

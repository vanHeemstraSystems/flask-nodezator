from app.extensions import db

class Node(db.Model):
    __tablename__ = 'node'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    node_type = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, ForeignKey('node.id')) # Foreign Key to Node
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())    
    children = db.relationship('Node', backref='nodes')  # One-to-many relationship with Node

    def __repr__(self):
        return f'<Node {self.title}>'
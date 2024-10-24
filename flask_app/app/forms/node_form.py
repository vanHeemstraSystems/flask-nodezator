from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class NodeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    node_type = StringField('Node Type')
    parent_id = SelectField('Parent Node', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class CursoForm(Form):
    nombre = StringField('Nombre del curso', validators=[DataRequired()])
    maestro_id = SelectField('Maestro', coerce=int)
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    id = HiddenField('id')
    nombre = StringField("Nombre", validators=[DataRequired(), Length(min=2, max=50)])
    apellidos = StringField( "Apellidos", validators=[DataRequired()])
    email = EmailField("Correo", validators=[DataRequired(), Email()])
    telefono = StringField('telefono')
    submit = SubmitField("Guardar")

class UserForm2(FlaskForm):
    id = HiddenField('id')
    matricula = StringField("Matrícula", validators=[DataRequired()])
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellidos = StringField("Apellidos", validators=[DataRequired()])
    especialidad = StringField("Especialidad", validators=[DataRequired()])
    email = EmailField("Correo", validators=[DataRequired(), Email()])
    submit = SubmitField("Guardar Maestro")
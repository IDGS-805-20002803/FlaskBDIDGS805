from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    nombre = StringField(
        "Nombre",
        validators=[DataRequired(), Length(min=2, max=50)]
    )

    apaterno = StringField(
        "Apellido Paterno",
        validators=[DataRequired()]
    )

    email = EmailField(
        "Correo",
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField("Guardar")

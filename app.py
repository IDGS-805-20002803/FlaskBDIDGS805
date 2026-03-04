from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from maestros.routes import maestros 
import forms
from models import db, Alumno

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    alumnos_list = Alumno.query.all()
    return render_template("index.html", form=create_form, alumnos=alumnos_list)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        alum = Alumno(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("Alumnos.html", form=create_form)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    id = request.args.get('id')
    alum1 = Alumno.query.get_or_404(id)
    create_form = forms.UserForm(obj=alum1) 

    if request.method == 'POST':
        alum1.nombre = request.form.get('nombre')
        alum1.apellidos = request.form.get('apellidos')
        alum1.email = request.form.get('email')
        alum1.telefono = request.form.get('telefono')
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    alum1 = Alumno.query.get_or_404(id)
    create_form = forms.UserForm(obj=alum1)

    if request.method == 'POST':
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template("eliminar.html", form=create_form, alumno=alum1)

@app.route("/detalles")
def detalles():
    id = request.args.get('id')
    alum1 = Alumno.query.get_or_404(id)
    return render_template("detalles.html", alumno=alum1)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
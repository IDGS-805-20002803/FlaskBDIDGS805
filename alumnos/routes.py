from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Alumno
import forms

alumnos = Blueprint('alumnos', __name__)

@alumnos.route("/alumnos_index")
def index():
    create_form = forms.UserForm(request.form)
    alumnos_list = Alumno.query.all()
    return render_template("alumnos/index.html", form=create_form, alumnos=alumnos_list)

@alumnos.route("/alumnos/nuevo", methods=['GET', 'POST'])
def nuevo_alumno():
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
        return redirect(url_for('alumnos.index'))
    return render_template("/alumnos/Alumnos.html", form=create_form)

@alumnos.route("/modificar", methods=['GET', 'POST'])
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
        return redirect(url_for('alumnos.index'))
    
    return render_template("/alumnos/modificar.html", form=create_form)

@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    alum1 = Alumno.query.get_or_404(id)
    create_form = forms.UserForm(obj=alum1)

    if request.method == 'POST':
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    
    return render_template("/alumnos/eliminar.html", form=create_form)

@alumnos.route("/detalles", methods=['GET', 'POST'])
def detalles():
    id = request.args.get('id')
    alum1 = Alumno.query.get_or_404(id)
    create_form = forms.UserForm(obj=alum1)
    return render_template("/alumnos/detalles.html", alumno=alum1)





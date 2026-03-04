from flask import render_template, request, redirect, url_for, flash
from models import db, Maestros
import forms
from . import maestros

@maestros.route("/maestros")
def lista_maestros():
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMest.html", maestros=maestros_list)

@maestros.route("/agregar", methods=['GET', 'POST'])
def agregar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST' and create_form.validate():
        maestro = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    return render_template("maestros/agregarMaestro.html", form=create_form)

@maestros.route("/detalles/<int:matricula>")
def detalles(matricula):
    maestro = Maestros.query.filter_by(matricula=matricula).first_or_404()
    return render_template("maestros/detalles.html", maestro=maestro)

@maestros.route("/editar/<int:matricula>", methods=['GET', 'POST'])
def editar(matricula):
    maestro = Maestros.query.filter_by(matricula=matricula).first_or_404()
    form = forms.UserForm2(obj=maestro)
    
    if request.method == 'POST' and form.validate():
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data
        maestro.matricula = form.matricula.data
        
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    
    return render_template("maestros/editar.html", form=form, maestro=maestro)

@maestros.route("/eliminar/<int:matricula>", methods=['GET', 'POST'])
def eliminar(matricula):
    maestro = Maestros.query.filter_by(matricula=matricula).first_or_404()
    form = forms.UserForm2()
    
    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    
    return render_template("maestros/eliminar.html", maestro=maestro, form=form)
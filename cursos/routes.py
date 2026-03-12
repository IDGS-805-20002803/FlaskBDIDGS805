from flask import Blueprint, render_template, redirect, url_for, request
from models import Alumno, Inscripcion, db, Cursos, Maestros
from cursos.forms import CursoForm

cursos_bp = Blueprint('cursos', __name__, url_prefix='/cursos')

@cursos_bp.route('/')
def index():
    cursos = Cursos.query.all()
    return render_template('cursos/index.html', cursos=cursos)

@cursos_bp.route('/crear', methods=['GET','POST'])
def crear():
    form = CursoForm()
    maestros_list = Maestros.query.all()
    form.maestro_id.choices = [(m.matricula, m.nombre) for m in maestros_list]

    if request.method == 'POST':
        curso = Cursos(
            nombre=request.form.get('nombre'),
            descripcion = request.form.get('descripcion'),
            maestro_id=request.form.get('maestro_id')
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template('cursos/crear.html', form=form, maestros=maestros_list)

@cursos_bp.route('/detalles/<int:id>')
def detalles(id):
    curso = Cursos.query.get_or_404(id)
    alumnos_list = Alumno.query.all()
    return render_template('cursos/detalles.html', curso=curso, alumnos_disponibles=alumnos_list)

@cursos_bp.route('/inscribir', methods=['GET', 'POST'])
def inscribir():
    alumnos = Alumno.query.all()
    cursos = Cursos.query.all()

    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        curso_id = request.form.get('curso_id')
        
        alumno = Alumno.query.get(alumno_id)
        curso = Cursos.query.get(curso_id)
        
        if alumno and curso:
            try:
                curso.alumnos.append(alumno)
                db.session.commit()
                return redirect(url_for('cursos.index'))
            except:
                db.session.rollback()
                return "Error: El alumno ya está en este curso o hubo un problema. <a href='/cursos/inscribir'>Intentar de nuevo</a>"

    return render_template('cursos/inscribir.html', alumnos=alumnos, cursos=cursos)


@cursos_bp.route('/agregar_alumno_rapido/<int:curso_id>', methods=['POST'])
def agregar_alumno_rapido(curso_id):
    alumno_id = request.form.get('alumno_id')
    nueva_inscripcion = Inscripcion(alumno_id=alumno_id, curso_id=curso_id)
    db.session.add(nueva_inscripcion)
    db.session.commit()
    return redirect(url_for('cursos.detalles', id=curso_id))
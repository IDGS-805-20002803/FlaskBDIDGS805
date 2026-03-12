from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from maestros.routes import maestros 
from cursos.routes import cursos_bp
from alumnos.routes import alumnos 
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


app.register_blueprint(maestros)
app.register_blueprint(cursos_bp)
app.register_blueprint(alumnos)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/")
def index():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run()
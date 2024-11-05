from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="conexion_post"
)
cursor = conexion.cursor(dictionary=True)

class AlumnoAPI:
    def __init__(self, app):
        app.add_url_rule('/', view_func=self.index, methods=['GET'])
        app.add_url_rule('/alumnos', view_func=self.get_alumnos, methods=['GET'])
        app.add_url_rule('/alumnos/agregar', view_func=self.add_alumno_form, methods=['GET'])
        app.add_url_rule('/alumnos', view_func=self.add_alumno, methods=['POST'])
        app.add_url_rule('/alumnos/<int:id_alum>/editar', view_func=self.update_alumno_form, methods=['GET'])
        app.add_url_rule('/alumnos/<int:id_alum>', view_func=self.update_alumno, methods=['POST'])
        app.add_url_rule('/alumnos/<int:id_alum>/eliminar', view_func=self.delete_alumno, methods=['GET'])

    def index(self):
        return render_template('index.html')

    def get_alumnos(self):
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()
        return render_template('alumnos.html', alumnos=alumnos)

    def add_alumno_form(self):
        return render_template('registro_alumno.html', alumno=None)

    def add_alumno(self):
        nuevo_alumno = request.form
        sql = "INSERT INTO alumnos (name, carrera, edad) VALUES (%s, %s, %s)"
        valores = (nuevo_alumno['name'], nuevo_alumno['carrera'], nuevo_alumno['edad'])
        cursor.execute(sql, valores)
        conexion.commit()
        return redirect(url_for('get_alumnos'))

    def update_alumno_form(self, id_alum):
        cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id_alum,))
        alumno = cursor.fetchone()
        return render_template('registro_alumno.html', alumno=alumno)

    def update_alumno(self, id_alum):
        datos_alumno = request.form
        sql = "UPDATE alumnos SET name = %s, carrera = %s, edad = %s WHERE id = %s"
        valores = (datos_alumno['name'], datos_alumno['carrera'], datos_alumno['edad'], id_alum)
        cursor.execute(sql, valores)
        conexion.commit()
        return redirect(url_for('get_alumnos'))

    def delete_alumno(self, id_alum):
        sql = "DELETE FROM alumnos WHERE id = %s"
        cursor.execute(sql, (id_alum,))
        conexion.commit()
        return redirect(url_for('get_alumnos'))

AlumnoAPI(app)

if __name__ == '__main__':
    app.run(debug=True)

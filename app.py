from flask import Flask, request, render_template, flash, redirect, url_for
from models import User, database
from forms import RegistrationForm
#prueba

app = Flask(__name__)

@app.before_request
def open_db():
    database.connect()

@app.after_request
def close_db(resp):
    database.close()
    return resp


@app.teardown_appcontext
def close_db_on_err(err):
    database.close()              

@app.route('/') 
def index(): 
    return ("<p><a href='/form'>Registrarme</a></p>"
            "<p><a href='/delete'>Borrar usuario</a></p>"
            "<p><a href='/patch'>Editar usuario</a></p>")


@app.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        msj = "Usuario registrado exitosamente"
        User(usuario=request.form["usuario"], clave=request.form["clave"]).save()
        return ("<p><a>Usuario registrado exitosamente</a></p>"
            "<p><a href='/'>Menu de inicio</a></p>")
    return render_template('form.html')


@app.route('/delete')
def user_cargar():
    user = User.select()
    resultado=list() 
    
    for x in user:
    	resultado.append(dict(id=x.id, user=x.usuario))

    return render_template("lista.html", user=resultado) 


@app.route('/delete/<int:id>', methods=('GET','DELETE'))
def delete_users(id):
    q = User.delete().where(User.id == id)
    q.execute()  # Remove the rows, return number of rows removed.
    return redirect(url_for('user_cargar'))

@app.route('/patch')
def patch():
    print ("Se abrio Editar usuario")
    user = User.select()
    resultado=list() 
    for x in user:
    	resultado.append(dict(id=x.id, user=x.usuario))
    return render_template("lista2.html", user=resultado) 


@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    data = User.get_by_id(id)
    return render_template("form2.html", id = data.id, usuario = data.usuario, clave = data.clave) 

@app.route('/edit/<int:id>', methods=['POST'])
def update_id(id):
    user = request.form["usuario"]
    clave = request.form["clave"]
    User.update().where(User.id == id).execute()
    return redirect(url_for('user_cargar'))


if __name__ == '__main__':
    app.run(debug=True)


from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/dojos')
def dashboard():
    allDojos = Dojo.getAllDojos()
    return render_template('dojos.html', dojos= allDojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name'],
    }
    Dojo.create_dojo(data)
    return redirect(request.referrer)

@app.route('/ninjas')
def ninjas():
    allDojos = Dojo.getAllDojos()
    return render_template('ninjas.html', dojos= allDojos)


@app.route('/dojosinfo')
def dojosinfo():
    allDojos = Dojo.getAllDojos()
    return render_template('dojosinfo.html', dojos= allDojos)

@app.route('/dojo/<int:id>')
def dojoninja(id):
    data= {
        'dojo_id': id,
    }
    allNinjas = Ninja.getAllNinjasOfDojo(data)
    return render_template('dojoninja.html', ninjas = allNinjas, dojo = Dojo.get_dojo_by_id(data))

@app.route('/ninjainfo')
def ninjainfo():
    allNinjas = Ninja.getAllNinjas()
    allDojos = Dojo.getAllDojos()
    return render_template('ninjainfo.html', ninjas= allNinjas, dojos = allDojos)




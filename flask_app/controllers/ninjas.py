from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create_ninja', methods=['POST'])
def create_ninjas():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }
    Ninja.create_ninja(data)
    return redirect(request.referrer)

@app.route('/ninjainfo')
def ninjasinfo():
    allNinjas = Ninja.getAllNinjas()
    allDojos = Dojo.getAllDojos()
    return render_template('ninjainfo.html', ninjas= allNinjas ,dojos = allDojos)

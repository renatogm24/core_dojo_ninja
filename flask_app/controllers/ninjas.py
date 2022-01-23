from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

from flask_app import app

@app.route('/ninjas/create')
def form_ninja():
    return render_template('/ninjas/ninja_form.html', all_dojos = Dojo.get_all())

@app.route('/ninjas/save',methods=['POST'])
def create_ninja():
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age'],
        "dojo_id":request.form['dojo_id']
    }
    dojo_id = request.form['dojo_id']
    Ninja.save(data)
    return redirect(f'/dojos/{dojo_id}')
from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo

from flask_app import app

@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def list_dojos():
    return render_template("dojos/index.html",all_dojos=Dojo.get_all())

@app.route('/dojos/<int:id>')
def dojo_with_ninjas(id):
    data = {
        "id": id,
    }
    return render_template("dojos/list_ninja.html",dojo=Dojo.get_dojo_with_ninjas(data))

@app.route('/dojos/create',methods=['POST'])
def create():
    data = {
        "name":request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')


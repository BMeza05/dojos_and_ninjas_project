from models.ninja import Ninja
from config.mysqlconnection import app
from flask import  redirect, request



@app.route('/create/ninja' ,methods=['POST'])
def ninjas():
        data = {
                "first_name" : request.form['first_name'],
                "last_name" : request.form['last_name'],
                "dojo" : request.form['dojo_id']
        }
        Ninja.save(data)
        return redirect('/dojos')
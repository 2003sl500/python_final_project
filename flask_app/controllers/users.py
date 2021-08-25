from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.client import Clients

@app.route('/')
def base_route():

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/clients')
def clients():
    
    return render_template('clients.html')

@app.route('/cases')
def cases():
    
    return render_template('cases.html')

@app.route('/motherboards')
def motherboards():
    
    return render_template('motherboards.html')

@app.route('/cpus')
def cpus():
    
    return render_template('cpus.html')

@app.route('/memory')
def memory():
    
    return render_template('memory.html')

@app.route('/monitors')
def monitors():
    
    return render_template('monitors.html')

@app.route('/keyboards_combo')
def keyboards_combo():
    
    return render_template('keyboards_combo.html')

@app.route('/storage')
def storage():
    
    return render_template('storage.html')
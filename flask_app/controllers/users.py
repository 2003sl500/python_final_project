from flask_app.models.case import Cases
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.client import Clients
from flask_app.models.case import Cases
from flask_app.models.motherboard import Motherboards
from flask_app.models.cpu import CPUS
from flask_app.models.memory import Memorys
from flask_app.models.storage import Storages
from flask_app.models.monitor import Monitors
from flask_app.models.keyboard import Keyboards
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def base_route():
    if 'cuid' in session:
        session.clear()
        return redirect('/')
    session['form'] = [{}]
    return render_template('index.html')

@app.route('/login')
def login():
    if 'cuid' in session:
        session.clear()
        return redirect('/')    
    return render_template('clients.html')

@app.route('/login/user', methods=['POST'])
def login_user():
    if 'cuid' in session:
        del session['cuid']
        return redirect('/')
        
    user_info = Clients.find_email(request.form['email_login'])
    print('********* user_info: ', user_info)
    if not user_info:
        session['email_login'] = request.form['email_login']
        flash("Invalid Email/Password", "login")
        return redirect('/login')
    
    if not Clients.validate_login(request.form):    
        session['email_login'] = request.form['email_login']
        return redirect('/login')
    
    if not bcrypt.check_password_hash(user_info[0]['password'], request.form['password_login']):
        flash("Invalid Email/Password", "login")
        return redirect('/login')
    
    session['cuid'] = user_info[0]['id']
    
    session['fname'] = user_info[0]['fname']
    
    return redirect('/user')

@app.route('/registration')
def registration():
    if 'cuid' in session:
        session.clear()
        return redirect('/')
    
    
    return render_template('clients.html')

@app.route('/register', methods=['POST'])
def register():
    if 'cuid' in session:
        session.clear()
        return redirect('/')
    
    if not Clients.validate_reg(request.form):
        session['form'] = request.form
        return redirect('/login')
    
    session.clear()
    session['fname'] = request.form['fname']
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
        'address': request.form['address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip': request.form['zip'], 
        'password': pw_hash
    }
    
    cuid = Clients.create(data)
    session['cuid'] = cuid
    
    return redirect('/user')

@app.route('/user')
def user():
    if 'cuid' not in session:  
        return redirect('/login')
    return render_template('user.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

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
    session['temp'] = [{'name': 'daniel', 'age': '48'}]
    print('********** temp:', session['temp'][0]['name'])
    return render_template('storage.html')

@app.route('/product_input')
def product_input():
    if 'cuid' not in session:
        session.clear()
        return redirect('/')
    elif (int)(session['cuid']) != 2:
        session.clear()
        return redirect('/')
    return render_template('product_input.html')

@app.route('/product_input/cases')
def input_cases():
    data = {
        'brand': request.form['brand'],
        'color': request.form['color'],
        'type': request.form['type'],
        'size': request.form['size']
    }
    Cases.create(data)
    return redirect('/product_input')

@app.route('/product_input/mb')
def input_mb():
    
    return redirect('/product_input')

@app.route('/product_input/cpus')
def input_cpus():
    
    return redirect('/product_input')

@app.route('/product_input/memory')
def input_memory():
    
    return redirect('/product_input')

@app.route('/product_input/storage')
def input_storage():
    
    return redirect('/product_input')

@app.route('/product_input/monitors')
def input_monitors():
    
    return redirect('/product_input')

@app.route('/product_input/keyboards')
def input_keyboards():
    
    return redirect('/product_input')
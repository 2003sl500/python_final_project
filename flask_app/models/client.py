from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


DB = 'python_proj'
CLIENTS = 'clients'

class Clients:
    def __init__(self, data):
        self.id = data['id']
        self.fname = data['fname']
        self.lname = data['lname']
        self.email = data['email']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = f'SELECT * FROM {CLIENTS};'
        results = connectToMySQL(DB).query_db(query)
        information = []
        for info in results:
            information.append( cls(info) )
        return information
    
    @classmethod
    def create(cls, data):
        query = f'INSERT INTO {CLIENTS}( fname, lname, email, address, city, state, zip, password, updated_at ) VALUES( %(fname)s, %(lname)s, %(email)s, %(address)s, %(city)s, %(state)s, %(zip)s, %(password)s, NOW() );'
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def find_email(cls, email):
        query = f'SELECT id, fname, lname, password FROM {CLIENTS} WHERE email = %(email)s;'
        email = {
            'email': email
        }
        return connectToMySQL(DB).query_db(query, email)
    
    @staticmethod
    def validate_login(form_data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_i]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (form_data['email_login'] == "") or (form_data['password_login'] == ""):
            flash("Email and Password are required", "login")
            is_valid = False
            return is_valid
        return is_valid
    
    @staticmethod
    def validate_reg(form_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_i]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if (form_data['fname'] == ""):
            flash("First Name is required", "fname")
            is_valid = False
        elif (len(form_data['fname']) < 3):
            flash("First name must be at least 3 characters", "fname")
            is_valid = False
        if (form_data['lname'] == ""):
            flash("Last Name is required", "lname")
        elif (len(form_data['lname']) < 3):
            flash("Last name must be at least 3 characters", "lname")
            is_valid = False
        if (form_data['email'] == ""):
            flash("Email is required", "email")
            is_valid = False
        if Clients.find_email(form_data['email']):
            flash("You are already registered", "email")
            is_valid = False
            return is_valid
        elif not (EMAIL_REGEX.match(form_data['email'])):
            flash("Email is not valid", "email")
            is_valid = False
        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters long", "password")
            is_valid = False
        elif (form_data['password']) != (form_data['conf_password']):
            flash("Password does not match Confirm Password", "conf_password")
            is_valid = False
        return is_valid
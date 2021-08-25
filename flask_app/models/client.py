from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

DB = 'python_proj'
CLIENTS = 'clients'

class Clients:
    def __init__(self, data):
        self.id = data['id']
        self.fname = data['fname']
        self.lname = data['lname']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
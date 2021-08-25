from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

DB = 'python_proj'
CPUS = 'cpus'

class Cpus:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.cores = data['cores']
        self.speed = data['brand']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.motherboard_id = data['motherboard_id']

   
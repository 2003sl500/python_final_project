from flask_app.config.mysqlconnection import connectToMySQL


DB = 'python_proj'
CASES = 'cases'

class Cases:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.color = data['color']
        self.type = data['type']
        self.size = data['size']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.client_id = data['client_id']
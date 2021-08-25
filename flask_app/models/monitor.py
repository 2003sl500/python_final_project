from flask_app.config.mysqlconnection import connectToMySQL


DB = 'python_proj'
MON = 'monitors'

class Monitors:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.size = data['size']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.motherboard_id = data['motherboard_id']

from flask_app.config.mysqlconnection import connectToMySQL


DB = 'python_proj'
KB = 'keyboards_mice'

class Keyboards:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.buttons = data['buttons']
        self.wireless = data['wireless']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.motherboard_id = data['motherboard_id']

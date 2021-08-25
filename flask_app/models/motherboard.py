from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

DB = 'python_proj'
MOTHER = 'motherboards'

class Motherboards:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.cpu_type = data['cpu_type']
        self.high_end = data['high_end']
        self.memory = data['memory']
        self.pci = data['pci']
        self.pcie = data['pcie']
        self.m2_drive = data['m2_drive']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.case_id = data['case_id']

from datetime import datetime, timedelta
from .User import User
import re

class Schedule:
    def __init__(self, objeto):
        self.id = objeto.get('id')
        self.name = objeto.get('name')
        self.division_id = objeto.get('division').get('id') if objeto.get('division') != None else None
        self.division_name = objeto.get('division').get('name') if objeto.get('division') != None else None
        self.version = objeto.get('version')
        self.date_created = objeto.get('dateCreated')
        self.date_modified = objeto.get('dateModified')
        self.created_by = objeto.get('modifiedBy')
        self.modified_by = objeto.get('createdBy')
        self.state = objeto.get('state')
        self.start = objeto.get('start')
        self.end = objeto.get('end')
        self.rrule = objeto.get('rrule')
        self.referenced_type = objeto.get('referencedType')
        self.format_date()
        
    def __str__(self):
        return f'Name: {self.name} - Version: {self.version}'
    
    def __eq__(self, schedule_id, schedule_name):
        return self.id == schedule_id and self.name == schedule_name
    
    def format_date(self):
        aux = re.split(r'[TZ.]',self.date_created)
        self.date_created = datetime.strptime(f'{aux[0]} {aux[1]}', '%Y-%m-%d %H:%M:%S') - timedelta(hours=3)
        aux = re.split(r'[TZ.]',self.date_modified)
        self.date_modified = datetime.strptime(f'{aux[0]} {aux[1]}', '%Y-%m-%d %H:%M:%S') - timedelta(hours=3)
        aux = re.split(r'[TZ.]',self.start)
        self.start = datetime.strptime(f'{aux[0]} {aux[1]}', '%Y-%m-%d %H:%M:%S')
        aux = re.split(r'[TZ.]',self.end)
        self.end = datetime.strptime(f'{aux[0]} {aux[1]}', '%Y-%m-%d %H:%M:%S')
        return None
    
    def get_users(self, objeto_created, objeto_modified):
        self.created_by = User(objeto_created)
        self.modified_by = User(objeto_modified)
        return None

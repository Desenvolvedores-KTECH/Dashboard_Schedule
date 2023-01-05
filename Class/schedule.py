from datetime import datetime
from .User import User

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
        self.date_created = datetime.strptime(self.date_created[:-5], '%Y-%m-%dT%H:%M:%S')
        self.date_modified = datetime.strptime(self.date_modified[:-5], '%Y-%m-%dT%H:%M:%S')
        self.start = datetime.strptime(self.start[:-5], '%Y-%m-%dT%H:%M:%S')
        self.end = datetime.strptime(self.end[:-5], '%Y-%m-%dT%H:%M:%S')
        return None
    
    def get_users(self, objeto_created, objeto_modified):
        self.created_by = User(objeto_created)
        self.modified_by = User(objeto_modified)
        return None

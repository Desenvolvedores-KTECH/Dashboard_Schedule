from datetime import datetime, timedelta
from .User import User
from .flow import Flow
import re

class Ivr:
    def __init__(self, objeto):
        self.id = objeto.get('id')
        self.name = objeto.get('name')
        self.division_id = objeto.get('division').get('id') if objeto.get('division') != None else None
        self.division_name = objeto.get('division').get('name') if objeto.get('division') != None else None
        self.date_created = objeto.get('dateCreated')
        self.date_modified = objeto.get('dateModified')
        self.created_by = objeto.get('createdBy')
        self.modified_by = objeto.get('modifiedBy')
        self.state = objeto.get('state')
        self.dnis = objeto.get('dnis')
        self.flow = None
        self.flow_id  = objeto.get('flowId')
        self.open_hours_flow_id = objeto.get('openHoursFlow').get('id') if objeto.get('openHoursFlow') != None else None
        self.open_hours_flow_name = objeto.get('openHoursFlow').get('name') if objeto.get('openHoursFlow') != None else None
        self.closed_hours_flow_id = objeto.get('closedHoursFlow').get('id') if objeto.get('closedHoursFlow') != None else None
        self.closed_hours_flow_name = objeto.get('closedHoursFlow').get('name') if objeto.get('closedHoursFlow') != None else None
        self.schedule_group_id = objeto.get('scheduleGroup').get('id') if objeto.get('scheduleGroup') != None else None
        self.schedule_group_name = objeto.get('scheduleGroup').get('name') if objeto.get('scheduleGroup') != None else None
        self.format_date()
        
    def __str__(self):
        return f'Name: {self.name} - State: {self.state}'
    
    def format_date(self):
        aux = re.split(r'[TZ.]',self.date_created)
        self.date_created = datetime.strptime(f'{aux[0]} {aux[1]}', '%Y-%m-%d %H:%M:%S') - timedelta(hours=3)
        aux = re.split(r'[TZ.]',self.date_modified)
        self.date_modified = datetime.strptime(f'{aux[0]} {aux[1]}', '%Y-%m-%d %H:%M:%S') - timedelta(hours=3)
        return None
    
    def get_users(self, objeto_created, objeto_modified):
        self.created_by = User(objeto_created)
        self.modified_by = User(objeto_modified)
        return None
    
    def get_flow(self, objeto_flow):
        self.flow = Flow(objeto_flow)
        return None
        
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
        self.flow_id  = objeto.get('flowId')
        self.open_hours_flow_id = objeto.get('openHoursFlow').get('id') if objeto.get('openHoursFlow') != None else None
        self.open_hours_flow_name = objeto.get('openHoursFlow').get('name') if objeto.get('openHoursFlow') != None else None
        self.closed_hours_flow_id = objeto.get('closedHoursFlow').get('id') if objeto.get('closedHoursFlow') != None else None
        self.closed_hours_flow_name = objeto.get('closedHoursFlow').get('name') if objeto.get('closedHoursFlow') != None else None
        self.schedule_group_id = objeto.get('scheduleGroup').get('id') if objeto.get('scheduleGroup') != None else None
        self.schedule_group_name = objeto.get('scheduleGroup').get('name') if objeto.get('scheduleGroup') != None else None
        
    def __str__(self):
        return f'Name: {self.name} - State: {self.state}'
        
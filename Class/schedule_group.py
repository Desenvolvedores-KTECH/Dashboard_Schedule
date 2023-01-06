class ScheduleGroup:
    def __init__(self, objeto):
        self.id = objeto.get('id')
        self.name = objeto.get('name')
        self.division_id = objeto.get('division').get('id') if objeto.get('division') != None else None
        self.division_name = objeto.get('division').get('name') if objeto.get('division') != None else None
        self.state = objeto.get('state')
        self.time_zone = objeto.get('timeZone')
        self.open_schedules_name = [(obj.get('id'),obj.get('name')) for obj in objeto.get('openSchedules')] if objeto.get('openSchedules') != None else None
        self.closed_schedules_name = [(obj.get('id'),obj.get('name')) for obj in objeto.get('closedSchedules')] if objeto.get('closedSchedules') != None else None
        self.holiday_schedules_name = [(obj.get('id'),obj.get('name')) for obj in objeto.get('holidaySchedules')] if objeto.get('holidaySchedules') != None else None
        self.edge_update_schedules_name = [(obj.get('id'),obj.get('name')) for obj in objeto.get('edgeUpdateSchedules')] if objeto.get('edgeUpdateSchedules') != None else None
    
    def __str__(self):
        return f'Name: {self.name} - State: {self.state}'
    
    def __eq__(self, schedule_group_id, schedule_group_name):
        return self.id == schedule_group_id and self.name == schedule_group_name
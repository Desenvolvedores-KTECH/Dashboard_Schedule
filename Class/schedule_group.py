class ScheduleGroup:
    def __init__(self, objeto):
        self.id = objeto.get('id')
        self.name = objeto.get('name')
        self.division_id = objeto.get('division').get('id')
        self.division_name = objeto.get('division').get('name')
        self.state = objeto.get('state')
        self.time_zone = objeto.get('timeZone')
        self.open_schedules_id = objeto.get('openSchedules').get('id')
        self.open_schedules_name = objeto.get('openSchedules').get('name')
        self.closed_schedules_id = objeto.get('closedSchedules').get('id')
        self.closed_schedules_name = objeto.get('closedSchedules').get('name')
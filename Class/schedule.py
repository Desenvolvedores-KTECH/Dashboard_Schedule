class Schedule:
    def __init__(self, objeto):
        self.id = objeto.get('id')
        self.name = objeto.get('name')
        self.division_id = objeto.get('division').get('id')
        self.division_name = objeto.get('division').get('name')
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
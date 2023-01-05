class User:
    def __init__(self, objeto):
        self.id = objeto.get('id')
        self.name = objeto.get('name')
        self.division_id = objeto.get('division').get('id')
        self.division_name = objeto.get('division').get('name')
        self.email = objeto.get('email')
        self.state = objeto.get('state')
        self.acd_auto_answer = objeto.get('acdAutoAnswer')
    
    def __str__(self):
        return f'Name: {self.name} - E-mail: {self.email}'
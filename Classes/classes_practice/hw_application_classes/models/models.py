from framework.models import Model

class Plant(Model):
    file = 'plants.json'

    def __init__(self, name, location):
        self.name = name
        self.location = location

class Employee(Model):
    file = 'employees.json'
    def __init__(self, name, email, plant_id, name_salon = ''):
        self.name = name
        self.email = email
        self.plant_id = plant_id
        self.name_salon = name_salon

    def save(self):
        plant = Plant.get_by_id(self.plant_id)
        if not plant:
            raise Exception('Plant not found')
        super(Employee).save()


class Salon(Model):
    file = 'salon.json'

    def __init__(self, name_salon):
        self.name_salon = name_salon
        self.count = 1
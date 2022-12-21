import datetime

class Human:
    def __init__(self, name, surname, age, birth_date):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = birth_date or datetime.datetime.now()

class HumanSerializer:
    def serialize(self, obj, format):
        pass

obj = Human('Oleksiy', 'Maksymiv', 30, datetime.date(1992, 11, 13))
print(obj.birth_date, type(obj.birth_date))
#HumanSerializer.serialize(obj, 'csv')  # 1992-11-13 => 13-11-1992
#HumanSerializer.serialize(obj, 'json') # 1992-11-13 => 1992-11-13 00:00:00

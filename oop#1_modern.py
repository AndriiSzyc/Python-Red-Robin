'''1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info'''
class Vehicle: #средство передвижения
    def __init__(self, max_speed, mileage): #атрибути
        self.max_speed = max_speed #макс скорость
        self.miliage = mileage #пробег

    def increase_speed(self, increase):#увеличить скорость
        self.increase = increase
        self.max_speed = self.max_speed + self.increase
        print(f'max speed up to {self.max_speed} km/h')
   
    def break_speed(self): #скорость торможения
        break_speed = (self.max_speed / 10) ** 2
        return print(f'braking speed at speed {self.max_speed} km/h = {break_speed} m')
 
    def mileage_info(self): #iнфа о пробеге
        print(f'mileage {self.miliage} km')
        
'''2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity'''
class Bus(Vehicle):
    def __init__(self, max_speed, mileage): #seating_capacity):
        super().__init__( max_speed, mileage)
    
    def seating_capacity(self, capacity): #сидячих
        self.capacity = capacity
        print(f'seating capacity = {self.capacity}')

etalon = Bus(80, 50000)
print(etalon.break_speed())
print(etalon.mileage_info())
print(etalon.seating_capacity(18))

'''5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject'''
class School:
    def __init__(self, get_school_id, number_of_student):
        self.get_school_id = get_school_id
        self.number_of_student = number_of_student

    def print_number_of_student(self):
        print(f'number of student: {self.number_of_student}')
    
    def school_address(self, address):
        self.address = address
        print(f'school address scohol № {self.get_school_id} :\n{self.address}')

    def main_subject(self, subject):
        self.subject = subject
        print(f'main subject: {self.subject}')
        
'''6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color'''
class ScholBus(School, Bus):
    def __init__(self, get_school_id, number_of_student, max_speed, mileage):
        #self.get_school_id = get_school_id
        #self.number_of_student = number_of_student
        self.max_speed = max_speed #макс скорость
        self.miliage = mileage #пробег
        
        super().__init__(get_school_id, number_of_student)
        #super().__init__(max_speed, mileage)

    def bus_school_color(self, color):
        self.color = color
        print(f'color bus {self.color}')
        
bus_for_school = ScholBus(3, 5000, 60, 200000)

print(bus_for_school.bus_school_color('yellow'))             
print(bus_for_school.school_address('Ukraine, Kiev region, m.Slavutich, ave.  Druzhby Narodiv, 1'))              
print(bus_for_school.print_number_of_student())
print(bus_for_school.break_speed())
print(bus_for_school.seating_capacity(18))
print(bus_for_school.mileage_info())


print(f'Dir bus_for_school:\n{dir(bus_for_school)}\n')

print(f'Type bus_for_school.bus_school_color: {type(bus_for_school.bus_school_color)}\n')

'''7. Поліморфізм: Створіть два класи: Bear, Wolf.
Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.'''
class Bear:
    def __init__(self, variety):
        self.variety = variety

    def print_variety(self):
        print(f'{self.variety}-bear')

    def eat(self):
        print('honey')
    
class Wolf:
    def __init__(self, variety):
        self.variety = variety

    def print_variety(self):
        print(f'{self.variety}-wolf')
    
    def eat(self):
        print('rabbit')

grizzly_bear = Bear('Grizzly')
grey_wolf = Wolf('Grey')

for animal in (grizzly_bear, grey_wolf):
    animal.eat()
    animal.print_variety()




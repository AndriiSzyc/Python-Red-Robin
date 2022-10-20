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
        #self.max_speed = max_speed
        print(f'braking speed at speed {self.max_speed} km/h = {(self.max_speed / 10) ** 2} m')
 
    def mileage_info(self): #iнфа о пробеге
        print(f'mileage {self.miliage} km')

honda = Vehicle(100, 30000)

honda.increase_speed(20)
honda.break_speed()
honda.mileage_info()

print('\n')
'''2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity'''

class Bus(Vehicle):
    #def __init__(self, max_speed, mileage): #seating_capacity):
    #self.max_speed = max_speed #макс скорость
    #self.miliage = mileage #пробег
    #self.seating_capacity = seating_capacity

    def seating_capacity(self, capacity): #сидячих
        self.capacity = capacity
        print(f'seating capacity = {self.capacity}')

marshrutka = Bus(80, 50000)

marshrutka.increase_speed(20)
marshrutka.break_speed()
marshrutka.mileage_info()
marshrutka.seating_capacity(12)

'''3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)'''

print(f'\nissubclass Bus from Vehicle = {issubclass(Bus, Vehicle)}')

'''4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus'''

scholl_bus = Bus(60, 10000)

print(f'\nisinstance scholl_bus from Vehicle = {isinstance(scholl_bus, Vehicle)}')

print(f'\nisinstance school_bus from Bus = {isinstance(scholl_bus, Bus)}')

print('\n')
'''5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject'''

class School:
    def __init__(self, get_school_id, number_of_student):
        self.get_school_id = get_school_id
        self.number_of_student = number_of_student

    def school_address(self, address):
        self.address = address
        print(f'school address:\n{self.address}')

    def main_subject(self, subject):
        self.subject = subject
        print(f'main subject: {self.subject}')

my_school = School(3, 5000)
my_school.school_address('Ukraine, Kiev region, m.Slavutich, ave.  Druzhby Narodiv, 1')
my_school.main_subject('chemistry')

print('\n')
'''6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color'''

class SchoolBus(School, Bus):
    def bus_school_color(self, color):
        self.color = color
        print(f'bus school color - {self.color}')

bus_for_school = SchoolBus((3, 5000),(60, 10000))

print(f'Dir bus_for_school:\n{dir(bus_for_school)}\n')

print(f'Type bus_for_school.bus_school_color: {type(bus_for_school.bus_school_color)}')

print('\n')
'''7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.'''

class Bear:
    def eat(self): #, eat):
        #self.eat = eat
        #print(self.eat)
        print('honey')

class Wolf:
    def eat(self): #, eat):
        #self.eat = eat
        #print(self.eat)
        print('rabbit')

grizzly_bear = Bear()
panda_bear = Bear()

#bear_common = (grizzly_bear, panda_bear)

#bear_common = tuple(map(lambda n: n.eat(),bear_common))

grey_wolf = Wolf()
red_wolf = Wolf()

#wolf_common = (grey_wolf, red_wolf)

common_variable = (grizzly_bear, grey_wolf, panda_bear, red_wolf )

common_variable = tuple(map(lambda n: n.eat(), common_variable))

print('\n')
'''Магічні методи:
Додатково:
8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи'''

class City:
    def __new__(cls, name, population):
        if population > 1500:
            obj = object.__new__(cls)
            return obj
        else:
            print(f'{name} Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population
        print(f'{self.name} Great city')

first_city = City('Slavutich', 25000)
second_city = City('Moskow', 1000)

print(f'\nisinstance first_city from City = {isinstance(first_city, City)}')

print(f'\nisinstance second_city from City = {isinstance(second_city, City)}') 

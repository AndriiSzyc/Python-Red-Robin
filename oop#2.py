#1. Make the class with composition.
class Laptop:

    def __init__(self):
        type_battery_1 = Battery('NiCd')
        type_battery_2= Battery('NiMH')
        type_battery_3 = Battery('Li-ion')
        self.types = [type_battery_1.types, type_battery_2.types, type_battery_3.types]

class Battery:

    def __init__(self, types):
        self.types = types

types_battery = Laptop()
print(types_battery.types)

#2. Make the class with aggregation

class Guitar:
    def __init__(self, strings):
        self.strings = strings.string_type

class GuitarString:
    def __init__(self, string_type):
        self.string_type = string_type

steel_string = GuitarString('Steel')
les_paul = Guitar(steel_string)
print(les_paul.strings)

#3 Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
class Calc:
    def __init__(self, num_1, num_2, num_3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

    def add_nums(self):
        return self.num_1 + self.num_2 +self.num_3

numbers = Calc(5, 6, 7)
print(numbers.add_nums())


#4*.
class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

#5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """

#6.
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """

#7. Create the same class (6) but using NamedTuple
#8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """
#9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

#10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
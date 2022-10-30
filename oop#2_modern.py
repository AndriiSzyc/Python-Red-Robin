'''пункт 5 - клас концерту написаний так, що при створенні його сутності я легко можу обійти перевірку,
цього не має бути '''


class Concert:
    max_visitors_num = 0

    def __init__(self):
        self.visitors_count = 0
        print(f'Create new instance. Visitors count = {self.visitors_count} ')
        print(f'Max visitors num = {Concert.max_visitors_num}')

    @property
    def visitors_count(self):
        return self.__visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors_count):
        if visitors_count > Concert.max_visitors_num:
            self.__visitors_count = Concert.max_visitors_num
        else:
            self.__visitors_count = visitors_count


Concert.max_visitors_num = 50

concert = Concert()
print(isinstance(concert, Concert))
print(concert.max_visitors_num)

concert.visitors_count = 1001
print(concert.visitors_count)

Concert.max_visitors_num = 500

concert.visitors_count = 1001
print(concert.visitors_count)

'''пункт 8 - треба було створити класичний клас із його репрезентацією, без використання dataclasses'''

class AddressBook:
    def __init__(self, key: str, name: str, phone_number: str, address: str,  email: str, birthday: str, age: str):
        self.key = key
        self.name = name
        self.phone = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key = {self.key}, name = {self.name}, phone_number = {self.phone}, address = {self.address}, ' \
               f'email = {self.email}, birthday = {self.birthday}, age = {self.age}) '

adbook = AddressBook('7', 'Andrii', '+38067', 'Slav', 'andrii@ukr.net', '12.08.XXXX', '38')
print(adbook)

'''пункт 9 - звісно просте сетання належної об'єкту змінної працює, але треба було використати setattr()'''

class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
person.age = 38
print(person.age)

setattr(person, 'age', 25)
print(person.age)

'''пункт 10 - знову, в початковому класі не має бути атрибута email, він має бути доданий за допомогою setattr(), 
а потім за допомогою getattr() значення того мейла присвоєно окремій змінній, яку прінтанути'''

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

test_student = Student(38, 'Andrii')
setattr(test_student, 'email', 'andrii@ukr.net')
#print(dir(test_student))
student_email = getattr(test_student, 'email')
print(student_email)
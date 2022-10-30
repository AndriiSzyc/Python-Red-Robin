'''пункт 5 - клас концерту написаний так, що при створенні його сутності я легко можу обійти перевірку,
цього не має бути '''


class Concert:
    max_visitors_num = 0

    def __new__(cls, visitors_count):
        if visitors_count == Concert.max_visitors_num:
            obj = object.__new__(cls)
            print(' == ')
            return obj
        else:
            print(f' Your visitors {visitors_count} is not max visitors num {Concert.max_visitors_num}')
            visitors_count = Concert.max_visitors_num
            obj = object.__new__(cls)
            print(' = ')
            print('visitors count = ', visitors_count)
            return obj

    @property
    def visitors_count(self):
        return self.__visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors_count):
        if visitors_count > Concert.max_visitors_num:
            self.__visitors_count = Concert.max_visitors_num
        else:
            self.__visitors_count = visitors_count

    def __init__(self, visitors_count):
        self.visitors_count = visitors_count
        print(f'Create new instance. Visitors count = {self.visitors_count} ')
        print(f'Max visitors num = {Concert.max_visitors_num}')


Concert.max_visitors_num = 50

concert = Concert(1001)
print(isinstance(concert, Concert))
print(concert.max_visitors_num)

concert.visitors_count = 1001
print(concert.visitors_count)

'''пункт 8 - треба було створити класичний клас із його репрезентацією, без використання dataclasses'''

'''пункт 9 - звісно просте сетання належної об'єкту змінної працює, але треба було використати setattr()'''

'''пункт 10 - знову, в початковому класі не має бути атрибута email, він має бути доданий за допомогою setattr(), 
а потім за допомогою getattr() значення того мейла присвоєно окремій змінній, яку прінтанути'''
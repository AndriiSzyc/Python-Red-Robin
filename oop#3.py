from abc import abstractmethod, ABC

'''1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
Iterator get numbers of first Fibonacci numbers
Example:'''


class FibonacciNumbers:
    def __init__(self, limiter=0, f1=0, f2=1):
        self.f1 = f1
        self.f2 = f2
        self.limiter = limiter
        print(self.f1)
        print(self.f2)

    def __iter__(self):
        return self

    def __next__(self):

        self.limiter -= 1
        if self.limiter > 0:
           self.f1, self.f2 = self.f2, self.f1 + self.f2
           return self.f2
        else:
            raise StopIteration

for i in FibonacciNumbers(10):
    print(i)

'''2.* Implement generator for Fibonacci numbers'''
def fibonacci(quantity):
    f1 = 0
    f2 = 1

    print(f'{f1}\n{f2}')

    while quantity > 0:
        f1, f2 = f2, f1 + f2
        quantity -= 1
        yield f2

fib = fibonacci(10)
for i in fib:
    print(i)


'''3. Write generator expression that returns square numbers of integers from 0 to 10'''

def generator(quantity):
    number = 0
    twice = 0
    while quantity > 0:
        twice = number ** 2
        number += 1
        quantity -= 1
        yield twice

gen = generator(10)
for i in gen:
    print(i)

'''4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.'''


class Laptop(ABC):

    @abstractmethod
    def Screen(self, size: int):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self, type_key: str):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self, manufacturer: str):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self, res: str):
        raise NotImplementedError

    @abstractmethod
    def Ports(self, amount: int):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self, variety: str):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def Screen(self, size):
        print(size)

    def Keyboard(self, type_key):
        print(type_key)

    def Touchpad(self, manufacturer):
        print(manufacturer)

    def WebCam(self, res):
        print(res)

    def Ports(self, amount):
        print(amount)

    def Dynamics(self, variety):
        print(variety)


my_laptop = HPLaptop('lenovo', 2012)
my_laptop.Touchpad('mechanical keyboard')
my_laptop.Ports(4)

'''5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
should be abstract.'''


class Car(ABC):

    def drive(self):
        print('i am drive')

    def stop(self):
        print('i am stop')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError

class Ford(Car):
    def __init__(self, body_type, engine, transmission):
        self.body_type = body_type
        self.engine = engine
        self.transmission = transmission

    def drive(self):
        print('i am drive')

    def stop(self):
        print('i am stop')

    def open_door(self):
        print('i am open door')

    def close_door(self):
        print('i am close door')

    def turn_on_light(self):
        print('i am turn on light')

    def turn_off_light(self):
        print('i am turn_off light')

    def enable_radio(self):
        print('i am enable radio')

    def disable_radio(self):
        print('i am disable radio')

car = Ford('sedan', 'diesel', 'automat')
car.drive()
car.stop()
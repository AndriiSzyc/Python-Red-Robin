from abc import abstractmethod, ABC

'''1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
Iterator get numbers of first Fibonacci numbers
Example:'''


class Fibonacci:
    def __init__(self, f1=1, f2=1):
        self.f1 = f1
        self.f2 = f2

    def fibonacci_sec(self):
        print(f'{self.f1}\n{self.f2}')
        for i in range(2, 10):
            self.f1, self.f2 = self.f2, self.f1 + self.f2
            print(self.f2)


fibonacci = Fibonacci()
fibonacci.fibonacci_sec()

'''for i in FibonacciNumbers(10):
    print(i)
0
1
1
2
3
5
8
13
21
34
55'''

'''2.* Implement generator for Fibonacci numbers

3. Write generator expression that returns square numbers of integers from 0 to 10

4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
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

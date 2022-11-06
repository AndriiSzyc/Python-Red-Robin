from datetime import date
from decimal import Decimal
from decorator import timer


class Employee:
    ROW_FORMAT = "| {:<30} | {:<10} | {:<10} | {:<10} |"
    ROW_LENGTH = 73
    OBJECT_LIST = []

    def __init__(
        self,
        name: str,
        start: date,
        rate: Decimal,
        taxes: int,
        end: date = date.today(),
    ):
        self.validation(name=name, start=start, end=end, rate=rate, taxes=taxes)
        self.name = name
        self._start = start
        self._rate = rate
        self._taxes = taxes
        self._end = end
        self._balance = self._recalculate_balance()
        print(f"{self.name} create!")
        Employee.OBJECT_LIST.append(self)

    @staticmethod
    def validation(name: str, start: date, end: date, rate: Decimal, taxes: int):
        if not end > start:
            raise ValueError("Start date cant be more than today")
        if not Decimal("100") > rate > Decimal("10"):
            raise ValueError("Rate must be between 10 and 100")
        if not 90 >= taxes > 1:
            raise ValueError("Taxes must be between 1 and 99")
        if not 20 >= len(name) > 2:
            raise ValueError("Naime must be from 2 and 20 characters")

    def days(self):
        return (self._end - self._start).days

    def how_long(self):
        return f"{self.name} works {self.days()} day(s)."

    def _recalculate_balance(self):
        self._balance = self._rate * self.days()
        return self._balance

    @timer(func_name="update_rate")
    def update_rate(self, new_rate):
        self._rate = new_rate
        self._balance = self._recalculate_balance()
        return self._rate

    @property
    def rate(self):
        return self._rate

    @classmethod
    def show_line(cls):
        print(cls.ROW_LENGTH * "-")

    @staticmethod
    def show_row(cls):
        _name = cls.how_long()
        _balance = cls._balance
        _taxes_pay = cls._taxes * cls.days()
        _salary = cls._balance - _taxes_pay
        data = [_name, _balance, _taxes_pay, _salary]
        print(cls.ROW_FORMAT.format(*data))

# HW #8
    @classmethod
    def show_header(cls):
        header = ["Name", "Balance", "Taxes Pay", "Salary"]
        print((cls.ROW_FORMAT.format(*header)))

    @classmethod
    @timer(func_name="show_tabel")
    def show_tabel(cls):
        Employee.show_line()
        Employee.show_header()
        Employee.show_line()
        for elem in Employee.OBJECT_LIST:
            Employee.show_row(elem)
            Employee.show_line()

    @classmethod
    def change_pay_all(cls):
        for elem in Employee.OBJECT_LIST:
            new_rate = Decimal(input(f"Enter new rate for {elem.name}: "))
            elem.update_rate(new_rate)

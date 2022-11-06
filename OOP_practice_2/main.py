from classes import Employee
from datetime import date
from decimal import Decimal




john = Employee(name="John", start=date(2022, 10, 5), rate=Decimal("11"), taxes=10)
elen = Employee(name="Elen", start=date(2022, 10, 3), rate=Decimal("15"), taxes=10)
kurt = Employee(name="Kurt", start=date(2022, 10, 2), rate=Decimal("14"), taxes=10)
sid = Employee(name="Sid", start=date(2022, 10, 4), rate=Decimal("13"), taxes=10)
ozzy = Employee(name="Ozzy", start=date(2022, 10, 6), rate=Decimal("20"), taxes=10)

john.update_rate(Decimal('10'))
print(john.days())
print(john.how_long())
print(john._balance)
print(john._rate)

Employee.show_line()
Employee.show_header()
Employee.show_line()
Employee.show_row(john)
Employee.show_line()

Employee.show_tabel()

Employee.change_pay_all()

Employee.show_tabel()

print(ozzy.rate)
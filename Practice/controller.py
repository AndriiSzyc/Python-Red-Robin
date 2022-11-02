from models.models import Plant, Employee, Salon


class Controller:

    @classmethod
    def start_menu(cls):
        while True:
            print('1. Add new plant \n'
            '2. Get all plants \n'
            '3. Get plant id \n'
            '4. Delete plant to id \n'
            '5. Add new employee \n'
            '6. Get all employee \n'
            '7. Get employee id \n'
            '8. Delete employee id\n'
            '9. Change salon for id employee\n'
            '10. ENTER to stop program \n')
            flag = input("Choose: ")
            match flag:
                case '1': cls.add_new_plant()
                case '2': cls.get_all_plants()
                case '3': cls.get_plant_id()
                case '4': cls.delete_plant_id()
                case '5': cls.add_new_employee()
                case '6': cls.get_all_employee()
                case '7': cls.get_employee_id()
                case '8': cls.delete_employee_id()
                case '9': cls.change_salon_for_id_employee()
                case '': break


    @classmethod
    def add_new_plant(cls):
        name = input('Type name of new plant: ')
        location = input('Type location of plant: ')
        plant = Plant(name, location)
        plant.save()

    @classmethod
    def get_all_plants(cls):
        plants = Plant.get_all()
        for plant in plants:
            print(plant['id'])
            print(plant['name'])
            print(plant['location'])

    @classmethod
    def get_plant_id(cls):
        id = int(input('Type id of plant: '))
        plant = Plant.get_by_id(id)
        print(plant['id'])
        print(plant['name'])
        print(plant['location'])

    @classmethod
    def delete_plant_id(cls):
        id = int(input('Type id of plant which you want to delete: '))
        Plant.delete(id)

    @classmethod
    def add_new_employee(cls):
        name = input('Type name of employee: ')
        email = input('Type email of employee: ')
        plant_id = int(input('Type id of plant: '))
        salon = input('Enter salon: ')
        employee = Employee(name, email, plant_id, salon)
        employee.save()

    @classmethod
    def get_all_employee(cls):
        employees = Employee.get_all()
        for employee in employees:
            print(employee['id'])
            print(employee['name'])
            print(employee['email'])
            print(employee['salon'])

    @classmethod
    def get_employee_id(cls):
        id = int(input('Type id of employee: '))
        employee = Employee.get_by_id(id)
        print(employee['id'])
        print(employee['name'])
        print(employee['email'])
        print(employee['salon'])

    @classmethod
    def delete_employee_id(cls):
        id = int(input('Type id of employee which you want to delete: '))
        Employee.delete(id)

    @classmethod
    def change_salon_for_id_employee(cls):
        name = input('Type new name of salon to employee: ')
        id_employee = int(input('Type id of employee: '))
        Salon.change_salon(name, id_employee)


if __name__ == '__main__':
    Controller.start_menu()
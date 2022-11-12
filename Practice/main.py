import logging
from models.models import Plant, Employee, Salon
from compare import Compare



#logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG)

while True:
    print('1. Add new plant \n'
          '2. Get all plants \n'
          '3. Get plant id \n'
          '4. Delete plant to id \n'
          '5. Add new employee \n'                     #no work for salon = done
          '6. Get all employee \n'
          '7. Get employee id \n'
          '8. Delete employee id\n'
          '9. Add new salon\n'                          #no work = done
          '10. Get all salon\n'                         #no work = done
          '11. Get salon by id employee\n'              #no work = done
          '12. Change salon for id employee\n'          #no work = done
          '13. Delete salon by id employee')            #no work = done


    logging.info('Menu printed!')
    try:
        flag = int(input('Choose: '))
    except ValueError:
        logging.error('User typed a symbol not NUMBER')
        print('You most to type number!!')
        continue
    compare = Compare('database/salon.json', 'database/employees.json')
    if flag == 1:
        name = input('Type name of new plant: ')
        location = input('Type location of plant: ')
        plant = Plant(name, location)
        plant.save()

    elif flag == 2:
        plants = Plant.get_all()
        for plant in plants:
            print(plant['id'])
            print(plant['name'])
            print(plant['location'])

    elif flag == 3:
        id = int(input('Type id of plant: '))
        plant = Plant.get_by_id(id)
        print(plant['id'])
        print(plant['name'])
        print(plant['location'])

    elif flag == 4:
        id = int(input('Type id of plant which you want to delete: '))
        Plant.delete(id)

    elif flag == 5:
        name = input('Type name of employee: ')
        email = input('Type email of employee: ')
        plant_id = int(input('Type id of plant: '))
        salon = input('Enter salon: ')
        employee = Employee(name, email, plant_id, salon)
        employee.save()
        compare.compare_lists()



    elif flag == 6:
        employees = Employee.get_all()
        for employee in employees:
            print(employee['id'])
            print(employee['name'])
            print(employee['email'])
            print(employee['salon'])

    elif flag == 7:
        id = int(input('Type id of employee: '))
        employee = Employee.get_by_id(id)
        print(employee['id'])
        print(employee['name'])
        print(employee['email'])
        print(employee['salon'])

    elif flag == 8:
        id = int(input('Type id of employee which you want to delete: '))
        Employee.delete(id)

    elif flag == 9: #Add new salon)))
        name_salon = input('Name of new salon: ')
        salon = Salon(name_salon)
        salon.save()
        compare.compare_lists()


    elif flag == 10: #Get all salon
        salons = Salon.get_all()
        for salon in salons:
            print(salon['id'])
            print(salon['name_salon'])



    elif flag == 11: #Get salon by id employee
        id = int(input('Type id of employee: '))
        employee = Employee.get_by_id(id)
        print(employee['id'])
        print(employee['salon'])


    elif flag == 12: #Change salon for id employee
        id_employee = int(input('Type id of employee: '))
        new_name = input(f'Enter new name salon for employeer id {id_employee}: ')
        Employee.change_salon(id_employee, new_name)
        compare.compare_lists()




    elif flag == 13: #Delete salon by id employee
        id = int(input('Type id of employee which salon you want to delete: '))
        Employee.delete_salon_emp_id(id)
        compare.compare_lists()










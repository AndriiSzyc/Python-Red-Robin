from abc import ABC
import os
import json
import logging

class Model(ABC):
    file = 'default.json'

    @staticmethod
    def get_data(path):
        try:
            file = open(path, 'r')
            data = json.loads(file.read())
            file.close()
        except FileNotFoundError:
            logging.warning('File not found')
            if not os.path.exists('database'):
                logging.warning('Folder database not exist ')
                os.mkdir('database')
            file = open(path, 'w')
            file.write('[]')
            file.close()
            logging.info('File created')
            file = open(path, 'r')
            data = json.loads(file.read())
            file.close()
        return data

    def save(self):

        data = self.get_data('database/' + self.file)  # з json в python сутність list()
        new_instance = self.__dict__ # створення dict
        if len(data) > 0:
            new_instance['id'] = data[-1]['id'] + 1
        else:
            new_instance['id'] = 1
        data.append(new_instance)
        self.save_data_to_file(data, 'database/' + self.file)


    @staticmethod
    def save_data_to_file(data, path):
        try:
            file = open(path, 'w')
            file.write(json.dumps(data))  # з python в json сутність
            file.close()
        except FileNotFoundError:
            logging.warning('File not found')
            if not os.path.exists('database'):
                logging.warning('Folder database not exist ')
                os.mkdir('dadabase')
            file = open(path, 'w')
            file.write(json.dumps(data))  # з python в json сутність
            file.close()
            logging.info('File created')

    @classmethod
    def get_all(cls):
        instances = cls.get_data('database/' + cls.file)
        return instances

    @classmethod
    def get_by_id(cls, id):
        instances = cls.get_data('database/' + cls.file)
        for instance in instances:
            if instance['id'] == id:
                return instance

    @classmethod
    def delete(cls, id):
        instances = cls.get_data('database/' + cls.file)
        for i in range(len(instances)):
            if instances[i]['id'] == id:
                del instances[i]
                break
        cls.save_data_to_file(instances, 'database/' + cls.file)

    @classmethod
    def change_salon(cls, id,  nwe_name_salon):             #for change Employee
        instances = cls.get_data('database/' + cls.file)
        for i in range(len(instances)):
            if instances[i]['id'] == id:
                instances[i]['name_salon'] = nwe_name_salon
                new_name = instances[i]['name_salon']
                break
        cls.save_data_to_file(instances, 'database/' + cls.file)
        return new_name

    @classmethod
    def delete_salon_emp_id(cls, id):                    #for Employee
        instances = cls.get_data('database/' + cls.file)
        for employee in instances:
            if employee['id'] == id:
                employee['name_salon'] = ''
                break
        cls.save_data_to_file(instances, 'database/' + cls.file)


    @classmethod
    def delete_salon_json(cls, name_salon):              #for change Salon
        instances = cls.get_data('database/' + cls.file)
        for i in range(len(instances)):
            if instances[i]['name_salon'] == name_salon:
                break
        cls.save_data_to_file(instances, 'database/' + cls.file)

    @classmethod
    def check_for_repetition(cls, new_salon):  #for Salon
        data = cls.get_data('database/' + cls.file)  # з json в python сутність list()
        count = 0
        for i in range(len(data)):
            if data[i]['name_salon'] == new_salon:
                data[i]['count'] += 1
                count += 1
                break
        if count == 0:
            return 1

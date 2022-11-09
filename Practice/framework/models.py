from abc import ABC
import json

class Model(ABC):
    file = 'default.json'

    @staticmethod
    def get_data(path):
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
        file = open(path, 'w')
        file.write(json.dumps(data))  # з python в json сутність
        file.close()

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
    def change_salon(cls, id,  nwe_name_salon):             #for Employee
        instances = cls.get_data('database/' + cls.file)
        for i in range(len(instances)):
            if instances[i]['id'] == id:
                instances[i]['salon'] = nwe_name_salon
                break
        cls.save_data_to_file(instances, 'database/' + cls.file)

    @classmethod
    def check_salon_for_repeat(cls, name_salon):             #for Salon
        data = cls.get_data('database/' + cls.file)
        if len(data) == 0:
            return 1
        else:
            for i in range(len(data)):
                if data[i]['name_salon'] == name_salon:
                    data[i]['count'] += 1
                    cls.save_data_to_file(data, 'database/' + cls.file)
                    break
                else:
                    return 1


    @classmethod
    def delete_salon_emp_id(cls, id):                    #for Employee
        instances = cls.get_data('database/' + cls.file)
        for employee in instances:
            if employee['id'] == id:
                employee['salon'] = ''
                break
        cls.save_data_to_file(instances, 'database/' + cls.file)





import json


class Compare:
    def __init__(self, first_json, second_json):
        self.first_json = first_json
        self.second_json = second_json

    @staticmethod
    def get_data(json_file):
        file = open(json_file, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    @staticmethod
    def save_data_to_file(path, data):
        file = open(path, 'w')
        file.write(json.dumps(data))  # з python в json сутність
        file.close()

    def compare_lists(self):
        data_1 = self.get_data(self.first_json)
        data_2 = self.get_data(self.second_json)

        set_ls1 = set()
        for i in range(len(data_1)):
            set_ls1.add(data_1[i]["name_salon"])

        set_ls2 = set()
        for i in range(len(data_2)):
            set_ls2.add(data_2[i]["name_salon"])

        result = list(set_ls1 ^ set_ls2)

        for i in range(len(data_1)):
            if data_1[i]["name_salon"] in result:
                del data_1[i]
                break

        for i in range(len(data_1)):
            count = 0
            for j in range(len(data_2)):
                if data_1[i]['name_salon'] == data_2[j]['name_salon']:
                    count += 1
                data_1[i]['count'] = count
        return self.save_data_to_file(self.first_json, data_1)

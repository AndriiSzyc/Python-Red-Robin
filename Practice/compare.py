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
        add_list = []
        for el1 in range(len(data_1)):
            count_salon = 0
            for el2 in range(len(data_2)):
                if data_1[el1]["name_salon"] == data_2[el2]["salon"]:
                    print(data_1[el1]["name_salon"])
                    add_list.append(data_1[el1])
                    count_salon += 1
                    print('count salon ', count_salon, '\n')
                    if count_salon > 1:
                        data_1[el1]['count'] = count_salon
                        add_list.append(data_1[el1]['count'])
                    else:
                        break

        add_list2 = []
        for item in add_list:
            if item not in add_list2:
                add_list2.append(item)
        #return add_list2
        return self.save_data_to_file(self.first_json, add_list2)


# compare = Compare('database/salon.json', 'database/employees.json')
# compare.compare_lists()
# print(compare.compare_lists())

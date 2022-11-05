import datetime
import csv
import json


class WriteLogs:
    count = 0
    txt_file = 'logs.txt'
    csv_file = 'logs.csv'
    json_file = 'logs.json'

    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)
        self.filename = filename

    def __enter__(self):
        self.write()
        self.write_scv()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write()
        self.file.close()
        self.write_scv()
        self.write_json()

    def write(self):
        with open(WriteLogs.txt_file, 'a') as logs:
            write_open = str(
                datetime.datetime.now()) + ' ' + self.filename + ' OPEN\n' if WriteLogs.count % 2 == 0 else str(
                datetime.datetime.now()) + ' ' + self.filename + ' CLOSE\n'
            logs.write(write_open)
        WriteLogs.count += 1

    @staticmethod
    def write_scv():
        with open(WriteLogs.txt_file, 'r') as txt_file:
            for line in txt_file:
                line = line.rstrip('\n')
                line = line.split(' ')
                line_sum = line[0] + ' ' + line[1]
                line = line[2:]
                line.insert(0, line_sum)
        with open(WriteLogs.csv_file, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(line)

    @staticmethod
    def write_json():
        count = 0
        last_open = ''
        with open(WriteLogs.csv_file, newline='') as scv_file:
            reader = csv.reader(scv_file, delimiter=',')
            for line in reader:
                line = ', '.join(line)
                if 'OPEN' in line:
                    count += 1
                    last_open = line
        line_date = last_open[:last_open.find(',')]
        name_file = last_open.split(', ')
        name_file = name_file[1]
        convert_dict = {name_file: {'count': count, 'last_time_opened': line_date}}
        with open(WriteLogs.json_file, 'w') as json_file:
            json.dump(convert_dict, json_file, indent=4)

import datetime
import csv
import json

#TASK 1
class WriteLogs:
    count = 0

    @classmethod
    def write(cls, time, file):
        cls.time = time
        cls.file = file
        with open('logs.txt', 'a') as logs:
            write_open = str(cls.time) + ' ' + cls.file + ' OPEN\n' if WriteLogs.count % 2 == 0 else str(cls.time) + ' ' + cls.file + ' CLOSE\n'
            logs.write(write_open)
            WriteLogs.count += 1


time_now = datetime.datetime.now()
read_file = 'file.txt'
with open(read_file, 'r') as file:
    WriteLogs.write(time_now, read_file)
    file.read()
    WriteLogs.write(time_now, read_file)

#TASK 2
def write_scv(file):
    with open(file, 'r') as txt_file:
        for line in txt_file:
            line = line.rstrip('\n')
            line = line.split(' ')
            line_sum = line[0] + ' ' + line[1]
            line = line[2:]
            line.insert(0, line_sum)
            #print(line)
            with open('logs.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(line)

scv_model = write_scv('logs.txt')

#TASK 3

def count_open(file):
    count = 0
    last_open = ''
    with open(file, newline='') as scv_file:
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
    with open('logs.json', 'w') as json_file:
        json.dump(convert_dict, json_file, indent=4)

json_model = count_open('logs.csv')
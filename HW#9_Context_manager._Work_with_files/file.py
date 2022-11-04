import datetime
import csv

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
            print(line)
            with open('logs.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(line)

scv_model = write_scv('logs.txt')

#TASK 3

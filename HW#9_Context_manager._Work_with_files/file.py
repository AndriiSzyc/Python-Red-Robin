import datetime

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





import datetime


class WriteLogs:
    file = None
    time = None
    count = 0

    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)
        self.filename = filename

    def __enter__(self):
        WriteLogs.write(datetime.datetime.now(), self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        WriteLogs.write(datetime.datetime.now(), self.filename)
        self.file.close()

    @classmethod
    def write(cls, time, filename):
        cls.time = time
        cls.file = filename
        with open('logs.txt', 'a') as logs:
            write_open = str(cls.time) + ' ' + cls.file + ' OPEN\n' if WriteLogs.count % 2 == 0 else str(
                cls.time) + ' ' + cls.file + ' CLOSE\n'
            logs.write(write_open)
            WriteLogs.count += 1


with WriteLogs('file.txt', 'r') as file_read:
    file_read.read()

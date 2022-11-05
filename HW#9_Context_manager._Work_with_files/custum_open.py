import datetime


class WriteLogs:
    file = None
    time = None
    count = 0

    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)
        self.filename = filename

    def __enter__(self):
        WriteLogs.write(self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        WriteLogs.write(self.filename)
        self.file.close()

    @classmethod
    def write(cls, filename):
        cls.file = filename
        with open('logs.txt', 'a') as logs:
            write_open = str(datetime.datetime.now()) + ' ' + cls.file + ' OPEN\n' if WriteLogs.count % 2 == 0 else str(
                datetime.datetime.now()) + ' ' + cls.file + ' CLOSE\n'
            logs.write(write_open)
        WriteLogs.count += 1


#with WriteLogs('file.txt', 'r') as file_read:
#    file_read.read()

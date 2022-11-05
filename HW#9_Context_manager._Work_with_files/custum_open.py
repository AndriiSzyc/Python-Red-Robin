import datetime


class WriteLogs:
    count = 0

    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)
        self.filename = filename

    def __enter__(self):
        self.write()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write()
        self.file.close()


    def write(self):
        with open('logs.txt', 'a') as logs:
            write_open = str(datetime.datetime.now()) + ' ' + self.filename + ' OPEN\n' if WriteLogs.count % 2 == 0 else str(
                datetime.datetime.now()) + ' ' + self.filename + ' CLOSE\n'
            logs.write(write_open)
        WriteLogs.count += 1


#with WriteLogs('file.txt', 'r') as file_read:
#    file_read.read()

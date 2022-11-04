import datetime

time_now = datetime.datetime.now()
read_file = 'file.txt'
with open(read_file, 'r') as file:
    #print('open')
    with open('logs.txt', 'a') as logs:
        write_open = str(time_now) + ' ' + read_file + ' OPEN\n'
        logs.write(write_open)
    file.read()
    #print('close')
    with open('logs.txt', 'a') as logs:
        write_close = str(time_now) + ' ' + read_file + ' CLOSE\n'
        logs.write(write_close)





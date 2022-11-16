#print(a)
#print('str' + 1)

#SyntaxError
#TypeError
#ValueError
#KeyError
#NameError

import logging
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG) #https://docs.python.org/3/howto/logging.html

'''type logging:
logging.info('program start working') коли логаєм якусь інфу
logging.error('Error')
logging.warning('Started to work on risky code')'''

logging.info('program start working')
try:
    logging.warning('Started to work on risky code')
    print(a)
except TypeError:
    logging.error('TypeError')
except NameError:
    logging.error('NameError')

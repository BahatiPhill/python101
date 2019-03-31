import logging

#Add filemode='w' to overwrite

logging.basicConfig(filename='sample.log', level=logging.INFO)


logging.debug('This is debug Message')
logging.info('Informational Message')
logging.error('An error has happened')
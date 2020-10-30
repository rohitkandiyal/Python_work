import logging

logging.basicConfig(filename='abc.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')

logging.debug("This is debug")
logging.info('This is info')
logging.warning('This is warning')
logging.error('This is error')

def abc():
    logging.info(abc.__name__, "This is function info")

abc

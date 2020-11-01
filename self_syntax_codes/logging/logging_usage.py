import logging

logging.basicConfig(filename='abc.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S')
a="defined"
logging.debug("This is debug")
logging.info('This is info')
logging.warning('This is warning')
logging.error('This is error {}'.format(a))


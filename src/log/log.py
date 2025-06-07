import logging
from constants.constants import LOG_FOLDER
def log():
    logging.basicConfig(
        filename=LOG_FOLDER / 'DataAnalytics.log',
        filemode='a',
        format='%(asctime)s - %(message)s ',
        level=logging.DEBUG,
    )
    return logging.getLogger()

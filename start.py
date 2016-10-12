import requests
import settings
import json
import os
import logging
import envoy


base_dir = settings.PATH
log_file_dir = settings.LOG_FILE_DIR
log_file = settings.LOG_FILE
directories = [base_dir, log_file_dir]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler(log_file)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def check_directories():
    '''
    Checks if the required
    directories exists
    '''
    for directoy in directories:
        try:
            os.makedirs(directoy)
        except OSError as os_err:
            logger.error("Error while creating directory ", os_err)
            if not os.path.isdir(directoy):
                # If the directpory is already present
                logger.info("Directory %s already present" % directoy)


def main():
    '''
    Brain of the automation
    '''
    check_directories()
    logger.info("Directory check completed")
    for i in xrange(0, 10001):
        logger.info("Got all the required job list %s" % i)


main()

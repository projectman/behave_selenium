import logging
import os
from datetime import datetime

LOGS = 'logs'


def custom_logger(log_level=logging.DEBUG, target_dir=LOGS) -> logging.Logger:
    """
    @param: log_level, str, level of log
    @param: target_dir, str, relative path of dir where log will be saved
    @return: logger, object of logger
    """

    logger = logging.getLogger()
    logger.setLevel(log_level)

    file_name = f'log_{get_date_time_string()}.txt'
    full_path = os.path.join(target_dir, file_name)
    file_handler = logging.FileHandler(full_path, mode='a')

    formatter = logging.Formatter(
        '%(asctime)s - %(module)-16s - %(levelname)-8s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def get_date_time_string() -> str:
    """
    :return: str date and time for using in file naming.
    """
    now = datetime.now()
    date = '_%s_%s_%s' % (now.year, now.month, now.day)
    time = '_%sH%sM%sS' % (now.hour, now.minute, now.second)
    return date + time


if __name__ == '__main__':
    custom_logger()

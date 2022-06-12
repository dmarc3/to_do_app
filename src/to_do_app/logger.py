""" Root logger setup module """
import sys
from datetime import datetime
import logging

__author__ = "Marcus Bakke"

# Define root logger settings
LOG_FORMAT = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
LOG_FILE = f'log_{datetime.today():%d-%m-%Y}.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)
CONSOLE = logging.StreamHandler(sys.stdout)
ROOT_LOGGER = logging.getLogger()
ROOT_LOGGER.addHandler(CONSOLE)

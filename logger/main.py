import json
import logging.config
from lib import functions

# import logging configuration from json file
with open('config/logging.json') as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)

# logger for current file
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # output warning in console
    logger.warning("Program start")
    # output info in log file
    logger.info("This message comes from the main module")
    functions.show()
    functions.show_error_msg()
    logger.warning("Program exit")
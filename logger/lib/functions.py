import logging

# logger for current file
logger = logging.getLogger(__name__)

def show():
    print("We are in function show!")
    logger.info("This message comes from the function module")

def show_error_msg():
    print("Throws an error message in logs")
    logger.error("There was an error!")

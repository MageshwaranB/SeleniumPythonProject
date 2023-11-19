"""For generating logs, first we have import the logging package, call the basicConfig funtion and pass the filename,
format and datefmt arguments
    format=defines how the log will be formatted
    datefmt = we are customizing the date format for asctime
    force=True, force: If this keyword argument is specified as true, any existing handlers attached
    to the root logger are removed and closed, before carrying out the configuration as specified
    by the other arguments.
in order to set the fields, use getLogger function, it returns the logger object"""

import logging


class LogGen:
    @staticmethod
    def generate_logs():
        logging.basicConfig(filename=".\\Logs\\automation.log", format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

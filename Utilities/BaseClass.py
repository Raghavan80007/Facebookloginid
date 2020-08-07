import pytest
import logging
import inspect

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)  # this will print the name of the test case or else it will take the root name
        filehandler = logging.FileHandler("login.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger



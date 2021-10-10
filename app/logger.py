"""
This is logging module.
It is used to create logs in console.
"""

import logging

logging.basicConfig(level=logging.INFO) #Controls log type

def log(obj):
    """
    Function used to log events.
    Will convert any object to string.
    """
    logger = logging.getLogger(__name__)
    logger.info(obj)
    return

if __name__=="__main__":
    pass
import logging
from datetime import datetime

def timer(name, namespace="timer"):
    """
    Make sure that the logger is set up correctly.  Use the below example for a simple setup

    import sys, logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    """
    logger = logging.getLogger(namespace)
    def first_wrapped(func):
        def wrapped_function(*args, **kargs):
            start_time = datetime.now()
            result = func(*args, **kargs)
            logger.debug("%s %s"%(name, datetime.now() - start_time))
            return result
        return wrapped_function
    return first_wrapped


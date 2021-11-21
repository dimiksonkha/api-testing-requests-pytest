import logging
import sys
import pytest
from pytest_reportportal import RPLogger, RPLogHandler

@pytest.fixture(scope="session")
def logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if hasattr(request.node.config,'py_test_service'):
        logging.setLoggerClass(RPLogger)
        rp_handeler = RPLogHandler(request.node.config.py_test_service)

        console_handeler = logging.StreamHandler(sys.stdout)
        console_handeler.setLevel(logging.INFO)
        logger.addHandler(console_handeler)

    else:
        rp_handeler = logging.StreamHandler(sys.stdout)

    rp_handeler.setLevel(logging.INFO)
    return logger





    

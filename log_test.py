from log import logger
import unittest


class TestLog(unittest.TestCase):
    def test_log(self):
        logger.debug("test")
        logger.info("test")

import unittest
from time import sleep

from Page.login.baiduPage import baiduPage

from log import Log

logger = Log()
# 这是unittest


class Myunit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basepage = baiduPage()


    def setUp(self):
        print('\n')
        logger.info('---------------Start to perform---------------')
        self.driver = self.basepage.open()
        self.basepage.max_window()

    def tearDown(self):
        logger.info('---------------Perform the end---------------')
        # sleep(2)


    @classmethod
    def tearDownClass(cls):
        sleep(1)
        cls.basepage.close()

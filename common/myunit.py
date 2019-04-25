import unittest
from time import sleep
from Page.baiduPage import baiduPage
from common.log import Log
logger = Log()

# 这是unittest
class Myunit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        print('\n')
        logger.info('---------------Start to perform---------------')
        self.basePage = baiduPage()
        self.basePage.open()
        self.basePage.max_window()

    def tearDown(self):
        self.basePage.close()
        logger.info('---------------Perform the end---------------')

    @classmethod
    def tearDownClass(cls):
        sleep(1)
        pass
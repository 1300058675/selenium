import unittest
from time import sleep
from common.log import Log
from Page.baiduPage import baiduPage
import os
from config import globalparam
logger = Log()
# 这是unittest
img_path = globalparam.img_path


class Myunit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basepage = baiduPage()
        cls.driver = cls.basepage.open()

    def setUp(self):
        print('\n')
        logger.info('---------------Start to perform---------------')
        self.basepage.max_window()

    def tearDown(self):
        logger.info('---------------Perform the end---------------')
        # sleep(2)

    @classmethod
    def tearDownClass(cls):
        sleep(1)
        cls.basepage.close()

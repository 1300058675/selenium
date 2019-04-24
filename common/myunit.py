import unittest
from time import sleep
from selenium import webdriver
from common.base import Base
from common.log import Log
logger=Log()

# 这是unittest
class Myunit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html')
        cls.driver.maximize_window()
        cls.zendao = Base(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()
        sleep(1)
        self.driver.refresh()
        print('\n')
        logger.info('开始执行')

    def tearDown(self):
        logger.info('执行结束\n')

    @classmethod
    def tearDownClass(cls):
        sleep(1)
        cls.driver.quit()
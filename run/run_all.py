import time
import unittest
from common.HTMLTestRunner_mn import HTMLTestRunner
from common.sendmail import SendMail
from config import globalparam

def add_img(self):
    self.imgs.append(self.driver.get_screenshot_as_base64())
    return True

def setUp(self):
    # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
    self.imgs = []
    self.addCleanup(self.cleanup)

def cleanup(self):
    pass

def all_case():
   # 待执行用例的目录
   case_dir = "..\\case"
   testcase = unittest.TestSuite()
   discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test1.py",
                                                   top_level_dir=None)

# discover 方法筛选出来的用例，循环添加到测试套件中
   for test_suite in discover:
       for test_case in test_suite:
       # 添加用例到 testcase
          testcase.addTest(test_case)
   print(testcase)
   now = time.strftime("%Y-%m-%d %H-%M-%S")
   report = globalparam.report_path + '\\' + now + ' TestResult.html'
   runer = HTMLTestRunner(title="测试报告",
                           description="测试结果",
                           stream=open(report, "wb"),
                           verbosity=2, save_last_try=True)  # retry=1失败重跑
   runer.run(discover)
   SendMail().send()


if __name__ == '__main__':
    all_case()
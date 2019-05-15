import unittest
from  BeautifulReport import BeautifulReport
from config import globalparam
import time
from common.sendmail import SendMail

def all_test():
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = now + ' TestResult.html'
    test_suite = unittest.defaultTestLoader.discover('..\\case', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=file_name, description='测试报告', log_path=globalparam.report_path)
    SendMail().send()

if __name__ == '__main__':
    all_test()


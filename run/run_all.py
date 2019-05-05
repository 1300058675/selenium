# import time
# import unittest
# from HTMLTestRunner_Chart import HTMLTestRunner
# from config import globalparam
#
#
# def all_case():
#     # 待执行用例的目录
#     case_dir = "..\\case"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_dir,
#                                                    pattern="test_*.py",
#                                                    top_level_dir=None)
#
# # discover 方法筛选出来的用例，循环添加到测试套件中
#     for test_suite in discover:
#         for test_case in test_suite:
#             # 添加用例到 testcase
#             testcase.addTest(test_case)
#
#     print(testcase)
#     now = time.strftime("%Y-%m-%d %H-%M-%S")
#     report = globalparam.report_path + '\\ TestResult.html'
#     runer = HTMLTestRunner(title="测试报告",
#                            description="测试结果",
#                            stream=open(report, "wb"),
#                            verbosity=2)  # retry=1失败重跑
#
#     runer.run(discover)
#     # SendMail().send()

#
# if __name__ == '__main__':
#     all_case()

import unittest
from  BeautifulReport import BeautifulReport
from config import globalparam
import time


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = now+' TestResult.html'
    test_suite = unittest.defaultTestLoader.discover('..\\case', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=file_name, description='测试报告', log_path=globalparam.report_path)


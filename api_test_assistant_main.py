import unittest
from pyunitreport import HTMLTestRunner
import parse_api_test_cases
import os
import time
from api_test_case import ApiTestCase
from parse_api_test_cases import TestCaseParser

test_suite_name = 'demo'

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tcp = TestCaseParser('demo_test_suite')
    test_cases_list = tcp.get_test_case_list()

    for test_case in test_cases_list:
        ApiTestCase.runTest.__doc__ = test_case['name']
        test = ApiTestCase(test_case)
        suite.addTest(test)


    test_report_folder_path = os.path.join(os.getcwd(), 'tests/reports/')
    if not os.path.exists(test_report_folder_path):
        os.makedirs(test_report_folder_path)
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_report_file_path = str(test_suite_name) + time
    kwargs = {
        "output": test_report_folder_path,
        "report_name": test_report_file_path
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(suite)
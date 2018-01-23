import unittest
from pyunitreport import HTMLTestRunner
import parse_api_test_cases
import os
import time

class ApiTestCase(unittest.TestCase):
    def __init__(self, testcase_dict):
        super(ApiTestCase, self).__init__()
        self.testcase_dict = testcase_dict

    def runTest(self):
        print(self.testcase_dict['url'])
        self.assertEqual(self.testcase_dict['status_code'], 200)


testcase_dict01 = {
    'name': 'test01',
    'url': "https://int-vebweb-vip.dev.activenetwork.com/api/internal/campaigns?agency_id=8809",
    'status_code': 200
}
testcase_dict02 = {
    'name': 'test02',
    'url': "https://int-vebweb-vip.dev.activenetwork.com/api/internal/campaigns?agency_id=8809",
    'status_code': 200
}
test_suite_name = 'demo'

if __name__ == '__main__':
    suite = unittest.TestSuite()
    ApiTestCase.runTest.__doc__ = 'testcase_dict01'
    test = ApiTestCase(testcase_dict01)

    suite.addTest(test)

    ApiTestCase.runTest.__doc__ = 'testcase_dict02'
    test = ApiTestCase(testcase_dict02)

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
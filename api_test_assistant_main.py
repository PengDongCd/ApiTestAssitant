import unittest
from pyunitreport import HTMLTestRunner
import parse_api_test_cases
import os
import time
from api_test_case import ApiTestCase
from parse_api_test_cases import TestCaseParser
import argparse
import logging

if __name__ == '__main__':
    # Argument Parse
    parser = argparse.ArgumentParser(
        description='API Test Assistant, Help you to do api test.')
    parser.add_argument(
        'test_suite_name', help="Please add your test suite's path"
    )
    args = parser.parse_args()
    test_suite_name = args.test_suite_name

    # create log file
    log_file__folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests/log/')
    if not os.path.exists(log_file__folder_path):
        os.makedirs(log_file__folder_path)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_log_file_path = os.path.join(log_file__folder_path, str(test_suite_name)+time_str+'.log')
    logging.basicConfig(filename=test_log_file_path, level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='w')

    logging.info("=========Start test execution!========")
    suite = unittest.TestSuite()
    tcp = TestCaseParser(test_suite_name)
    test_cases_list = tcp.get_test_case_list()
    logging.info("Got est cases list of {test_suite_name}".format(test_suite_name=test_suite_name))

    for test_case in test_cases_list:
        ApiTestCase.runTest.__doc__ = test_case['name']
        test = ApiTestCase(test_case)
        suite.addTest(test)
        logging.info("Added {tc_name} to test suite".format(tc_name=test_case['name']))

    test_report_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests/reports/')
    if not os.path.exists(test_report_folder_path):
        os.makedirs(test_report_folder_path)
        logging.info("Report Folder Created at {path}".format(path=test_report_folder_path))
    else:
        logging.info("Report Folder already exists at {path}".format(path=test_report_folder_path))

    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_report_file_path = str(test_suite_name) + time_str
    kwargs = {
        "output": test_report_folder_path,
        "report_name": test_report_file_path
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(suite)
    logging.info("Test suite execution done!")

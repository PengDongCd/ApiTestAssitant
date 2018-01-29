import logging
import yaml
import os
import io

class TestCaseParser:

    def __init__(self, test_suite_name):
        self.test_suite_name = test_suite_name
        self.file_path = ""

    def get_file_path_by_test_suite_name(self):
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests/test_cases_list/' + str(self.test_suite_name) + '.yml')
        return  self.file_path

    def get_test_case_list(self):
        self.get_file_path_by_test_suite_name()
        with io.open(self.file_path, 'r', encoding='utf-8') as stream:
            test_case_list = yaml.load(stream)
            logging.info("Load config file")
            for test_case in test_case_list:
                yield test_case['test']
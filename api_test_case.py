import unittest
import requests
import urllib.parse
import response_parser
from test_validation import TestValidation

class ApiTestCase(unittest.TestCase):
    def __init__(self, testcase_dict):
        super(ApiTestCase, self).__init__()
        self.testcase_dict = testcase_dict

    def runTest(self):
        kwargs = self.testcase_dict['request_params']
        url = self.testcase_dict['host'] + self.testcase_dict['api']
        if self.testcase_dict['qurey_params']:
            query_params = urllib.parse.urlencode(self.testcase_dict['qurey_params'])
            url += '?' + query_params
        response = requests.request(self.testcase_dict['method'], url, **kwargs)
        tv = TestValidation(self.testcase_dict, response)
        for validation_tuple in tv.get_validation():
            if validation_tuple[0] == 'eq':
                self.assertEqual(validation_tuple[1], validation_tuple[2])
            elif validation_tuple[0] == 'gt':
                self.assertGreater(validation_tuple[1], validation_tuple[2])
            elif validation_tuple[0] == 'ge':
                self.assertGreaterEqual(validation_tuple[1], validation_tuple[2])
            elif validation_tuple[0] == 'lt':
                self.assertLess(validation_tuple[1], validation_tuple[2])
            elif validation_tuple[0] == 'le':
                self.assertLessEqual(validation_tuple[1], validation_tuple[2])
            elif validation_tuple[0] == 'ge':
                self.assertGreaterEqual(validation_tuple[1], validation_tuple[2])

import unittest
import requests
import urllib.parse

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
        print(response.text)
import unittest

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

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test = ApiTestCase(testcase_dict01)
    suite.addTest(test)
    test = ApiTestCase(testcase_dict02)
    suite.addTest(test)
    runner = unittest.TextTestRunner()
    runner.run(suite)
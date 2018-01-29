import logging
import re
from response_parser import ResponseParser

class TestValidation:
    def __init__(self, testcase_dict, response):
        self.validations = testcase_dict.get('validations')
        self.response = response

    def get_validations(self):
        for validation in self.validations:
            yield validation

    def get_response_body_dict(self):
        response_body_dict = ResponseParser(self.response).response_body()
        return response_body_dict

    def get_check_value_from_response_body(self, check_str):
        response_body_dict = self.get_response_body_dict()
        temp_dict = response_body_dict
        layers = check_str.split('>>')
        index_pattern = re.compile(r'(?<=\[)\d+(?=\])')
        for layer in layers:
            if isinstance(temp_dict, dict):
                if layer in temp_dict:
                    temp_dict = temp_dict.get(layer)
                else:
                    print("there is no key %s", layer)
                    return None
            elif isinstance(temp_dict, list):
                if index_pattern.search(layer):
                    index = int(index_pattern.search(layer).group())
                    temp_dict = temp_dict[index]
            else:
                print("Data type is not correct")
        return temp_dict

    def get_validation(self):
        for validation in self.get_validations():
            if validation['check'] == 'status_code':
                actual_result = self.response.status_code
            else:
                actual_result = self.get_check_value_from_response_body(validation['check'])
            logging.info("Validation item {} got!".format(validation['check']))
            yield (validation['comparator'], actual_result, validation['expected'])



from response_parser import ResponseParser

class TestValidation:
    def __init__(self, testcase_dict, response):
        self.validations = testcase_dict.get('validations')
        self.response = response

    def parse_validations(self):
        for validation in self.validations:
            value_layer

    def get_response_body_dict(self):
        response_body_dict = ResponseParser(self.response).response_body
        return response_body_dict

    def get_check_value_from_response_body(self, check_str):
        response_body_dict = self.get_response_body_dict()
        temp_dict = response_body_dict
        layers = check_str.split('.')
        for layer in layers:
            if isinstance(temp_dict, dict):
                if temp_dict.has_key(layer):
                    temp_dict = temp_dict.get(layer)
                else:
                    print("there is no key %s", layer)
            elif isinstance(temp_dict, list):
                temp_dict = temp_dict[0]
            else:
                print("Data type is not correct")
        return temp_dict

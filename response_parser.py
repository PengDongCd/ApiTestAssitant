import json

class ResponseParser:
    def __init__(self, repsonse):
        self.repsonse = repsonse


    def status_code(self):
        self.status_code = self.repsonse.get('status_code')
        return self.status_code

    def response_body(self):
        self.response_body = json.loads(self.repsonse)
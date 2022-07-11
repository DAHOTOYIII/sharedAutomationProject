import requests
import json

class API:
    def __int__(self, endpoint, method, headers, payload):
        self.url = ''
        self.headers ={}
        self.payload = {}
    def simpleGet(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        result = json.loads(response.text)
        return result
    def simplePost(self):
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        result = json.loads(response.text)
        return result

    def simplePut(self):
        result =''
        return result

class Auth:
    def __int__(self):
        pass
    def apiKeyAuth(self):
        pass
    def userAuth(self):
        pass

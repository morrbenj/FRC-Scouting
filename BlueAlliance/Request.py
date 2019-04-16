import json

class Client:


    def __init__(self):





class APIClient():

    BASE_URL = 'www.thebluealliance.com/api/v3/'

    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/vnd.api+json'})
        self.url = furl.furl()
        self.session.headers.update({'Authorization': 'Bearer ' + api_key})
        self.url.set(path=self.BASE_URL)

    def request(self, endpoint):
        response = self.session.get(endpoint, timeout=DEFAULT_TIMEOUT)

        if response.status_code != self.API_OK:
            exception = self.API_ERRORS_MAPPING.get(
                response.status_code, exceptions.APIError)
            raise exception()

        return json.loads(response.text)

class FIRSTClient():

    BASE_URL = ''

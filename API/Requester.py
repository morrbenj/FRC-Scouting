import json
import furl
import requests
from . import Exceptions

class Client:

    API_OK = 200
    API_ERRORS_MAPPING = {
        304: Exceptions.NoDataError,
        400: Exceptions.InvalidParameterError,
        401: Exceptions.UnauthorizedError,
        404: Exceptions.InvalidEventError,
        500: Exceptions.InternalServerError,
        501: Exceptions.InvalidPatternError,
        503: Exceptions.UnavailableError
    }
    def __init__(self, base_url):
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/vnd.api+json'})
        self.url = furl.furl()
        self.session.headers.update({'Authorization': 'Bearer ' + api_key})
        self.url.set(path=self.BASE_URL)

    def request(self, endpoint):
        response = self.session.get(endpoint)

        if response.status_code != self.API_OK:
            e = self.API_ERRORS_MAPPING.get(response.status_code, Exceptions.APIError)
            raise e()

        return json.loads(response.text)

class FIRSTClient(Client):
    def __init__(self):
        super(self)


class BlueAllianceClient(Client):
    def __init__(self):
        super(self)

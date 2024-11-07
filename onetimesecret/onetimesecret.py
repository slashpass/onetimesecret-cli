import requests
from requests.auth import HTTPBasicAuth

URL_TEMPLATE = "https://{}.onetimesecret.com"

class OneTimeSecretError(Exception):
    def __init__(self, message, status_code=None):
        self.status_code = status_code
        super().__init__(f"{message} (Status code: {status_code})" if status_code else message)

class OneTimeSecretCli(object):
    def create_link(self, secret, ttl=900):
        auth = HTTPBasicAuth(self.user, self.key) if self.user and self.key else None
        response = requests.post(
            f"{self.url}/api/v1/share",
            data={"secret": secret, "ttl": ttl},
            auth=auth,
        )
        self._handle_response_errors(response)

        return f'{self.url}/secret/{response.json()["secret_key"]}'

    def _handle_response_errors(self, response):
        if response.status_code != 200 or "secret_key" not in response.json():
            message = response.json().get("message", "Unknown error")
            raise OneTimeSecretError(message, status_code=response.status_code)

    def __init__(self, user=None, key=None, region="us", url=URL_TEMPLATE):
        self.key = key
        self.user = user
        self.url = url.format(region)

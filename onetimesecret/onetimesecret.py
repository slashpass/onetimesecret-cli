import requests
from requests.auth import HTTPBasicAuth

# Default base URL template with region
URL_TEMPLATE = "https://{}.onetimesecret.com"


class OneTimeSecretCli(object):
    def create_link(self, secret, ttl=900):
        response = requests.post(
            f"{self.url}/api/v1/share",
            data={"secret": secret, "ttl": ttl},
            auth=HTTPBasicAuth(self.user, self.key),
        )

        return f'{self.url}/secret/{response.json()["secret_key"]}'

    def __init__(self, user, key, url=URL_TEMPLATE, region="us"):
        self.key = key
        self.user = user
        self.url = url.format(region)  # URL dynamically includes region
import requests
from requests.auth import HTTPBasicAuth

# Default base URL template with region
URL_TEMPLATE = "https://{}.onetimesecret.com"


class OneTimeSecretCli(object):
    def create_link(self, secret, ttl=900):
        response = requests.post(
            "{}/api/v1/share".format(self.url),
            data={"secret": secret, "ttl": ttl},  # 900 ttl => 15 minutes
            auth=HTTPBasicAuth(self.user, self.key),
        )

        return "{}/secret/{}".format(self.url, response.json()["secret_key"])

    def __init__(self, user, key, url=URL_TEMPLATE, region="us"):
        self.key = key
        self.url = url
        self.user = user
        self.url = URL_TEMPLATE.format(region)  # URL dynamically includes region
import requests
from requests.auth import HTTPBasicAuth

URL = "https://onetimesecret.com"


class OneTimeSecretCli(object):
    def create_link(self, secret, ttl=900):
        response = requests.post(
            "{}/api/v1/share".format(self.url),
            data={"secret": secret, "ttl": ttl},  # 900 ttl => 15 minutes
            auth=HTTPBasicAuth(self.user, self.key),
        )

        return "{}/secret/{}".format(self.url, response.json()["secret_key"])

    def __init__(self, user, key, url=URL):
        self.key = key
        self.url = url
        self.user = user

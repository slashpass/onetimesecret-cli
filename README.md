# onetimesecret-cli

A simple Python client for interacting with the [OneTimeSecret API](https://docs.onetimesecret.com/docs/rest-api), allowing you to securely share secrets with a customizable expiration time and region support.

# Installation

Install via pip:

`pip install onetimesecret`

# Usage

To use the OneTimeSecretCli client, import the class and initialize it with your OneTimeSecret API credentials. You can optionally specify a default region (e.g., "us" or "eu").

```
from onetimesecret import OneTimeSecretCli

# Replace with your OneTimeSecret credentials and preferred region
ONETIMESECRET_USER = "your_username"
ONETIMESECRET_KEY = "your_api_key"
REGION = "us"  # Default region, can be "us" or "eu"

# Initialize the client
cli = OneTimeSecretCli(ONETIMESECRET_USER, ONETIMESECRET_KEY, REGION)

# Create a link for a secret message with a specified Time-to-Live (TTL)
link = cli.create_link("Your secret message here")
print("Secret link:", link)
```

# Parameters

## Initialization

`cli = OneTimeSecretCli(ONETIMESECRET_USER, ONETIMESECRET_KEY, REGION)`

- ONETIMESECRET_USER (str, optional): Your OneTimeSecret API username (usually your account email).
- ONETIMESECRET_KEY (str, optional): Your OneTimeSecret API key.
- REGION (str, optional): The region subdomain to use for API requests. Defaults to "us". Use "eu" for Europe. See Onetimesecret's website for the latest regions available.

### Examples:

```
# US region (default)
cli = OneTimeSecretCli("user@email.com", "api-key")
# EU region
cli = OneTimeSecretCli("user@email.com", "api-key", "eu")
# Anonymous Request (default region: US)
cli = OneTimeSecretCli()
```

## Creating a Link

`create_link(secret, ttl=900)`

- secret (str): The secret message you want to securely share.
- ttl (int, optional): The time-to-live for the secret in seconds (e.g., 900 for 15 minutes). Defaults to 900 seconds.

# Expected Output

Running the example code will print a secure link that can be shared:

Secret link: https://us.onetimesecret.com/secret/xxxxxxxxxxx

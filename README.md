# onetimesecret-cli

A simple python client to use the onetimesecret API https://onetimesecret.com/docs/api

## Install

`pip install onetimesecret`

## Ussage

```
from onetimesecret import OneTimeSecretCli

cli = OneTimeSecretCli(ONETIMESECRET_USER, ONETIMESECRET_KEY)
cli.create_link("secret") # return a link like https://onetimesecret.com/secret/xxxxxxxxxxx
```

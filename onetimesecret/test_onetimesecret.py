import pytest
from unittest import mock
from requests.models import Response
from requests.auth import HTTPBasicAuth
from onetimesecret import OneTimeSecretCli, OneTimeSecretError


@pytest.fixture
def mock_post():
    with mock.patch("requests.post") as mock_post:
        yield mock_post


def test_create_link_success(mock_post):
    # Arrange
    mock_response = mock.Mock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"secret_key": "abc123"}
    mock_post.return_value = mock_response

    cli = OneTimeSecretCli(user="user", key="key")

    # Act
    result = cli.create_link("my_secret")

    # Assert
    assert result == "https://us.onetimesecret.com/secret/abc123"
    mock_post.assert_called_once_with(
        "https://us.onetimesecret.com/api/v1/share",
        data={"secret": "my_secret", "ttl": 900},
        auth=HTTPBasicAuth("user", "key"),
    )


def test_create_link_no_auth(mock_post):
    # Arrange
    mock_response = mock.Mock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"secret_key": "abc123"}
    mock_post.return_value = mock_response

    cli = OneTimeSecretCli()  # No user, no key

    # Act
    result = cli.create_link("my_secret")

    # Assert
    assert result == "https://us.onetimesecret.com/secret/abc123"
    mock_post.assert_called_once_with(
        "https://us.onetimesecret.com/api/v1/share",
        data={"secret": "my_secret", "ttl": 900},
        auth=None,
    )


def test_create_link_error(mock_post):
    # Arrange
    mock_response = mock.Mock(spec=Response)
    mock_response.status_code = 400
    mock_response.json.return_value = {"message": "Bad Request"}
    mock_post.return_value = mock_response

    cli = OneTimeSecretCli(user="user", key="key")

    # Act & Assert
    with pytest.raises(OneTimeSecretError) as exc_info:
        cli.create_link("my_secret")
    
    assert str(exc_info.value) == "Bad Request (Status code: 400)"
    mock_post.assert_called_once_with(
        "https://us.onetimesecret.com/api/v1/share",
        data={"secret": "my_secret", "ttl": 900},
        auth=HTTPBasicAuth("user", "key"),
    )


def test_create_link_missing_secret_key(mock_post):
    # Arrange
    mock_response = mock.Mock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {}  # No "secret_key"
    mock_post.return_value = mock_response

    cli = OneTimeSecretCli(user="user", key="key")

    # Act & Assert
    with pytest.raises(OneTimeSecretError) as exc_info:
        cli.create_link("my_secret")
    
    assert str(exc_info.value) == "Unknown error (Status code: 200)"
    mock_post.assert_called_once_with(
        "https://us.onetimesecret.com/api/v1/share",
        data={"secret": "my_secret", "ttl": 900},
        auth=HTTPBasicAuth("user", "key"),
    )


def test_handle_no_auth(mock_post):
    # Arrange
    mock_response = mock.Mock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"secret_key": "def456"}
    mock_post.return_value = mock_response

    cli = OneTimeSecretCli(user=None, key=None, region="eu")

    # Act
    result = cli.create_link("another_secret")

    # Assert
    assert result == "https://eu.onetimesecret.com/secret/def456"
    mock_post.assert_called_once_with(
        "https://eu.onetimesecret.com/api/v1/share",
        data={"secret": "another_secret", "ttl": 900},
        auth=None,
    )
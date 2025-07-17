# tests/test_auth.py

import pytest
from unittest.mock import patch, MagicMock
from fiskaly_sdk.client import FiskalyClient
from fiskaly_sdk.exceptions import FiskalyAuthError

@patch("fiskaly_sdk.api.auth.requests.Session.post")
def test_authenticate_success(mock_post, client):
    # Simula respuesta exitosa de autenticación
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "content": {
            "access_token": {
                "bearer": "mocked_token",
                "expires_at": 9999999999
            }
        }
    }

    token = client.authenticate()
    assert token == "mocked_token"
    assert client.get_bearer_token() == "mocked_token"

@patch("fiskaly_sdk.api.auth.requests.Session.post")
def test_authenticate_fail(mock_post, client):
    # Simula error de autenticación
    mock_post.return_value.status_code = 401
    mock_post.return_value.json.return_value = {"message": "Unauthorized"}

    with pytest.raises(FiskalyAuthError):
        client.authenticate()

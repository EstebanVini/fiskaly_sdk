import pytest
from unittest.mock import patch
from fiskaly_sdk.client import FiskalyClient # type: ignore
from fiskaly_sdk.exceptions import FiskalyAuthError # type: ignore

@pytest.fixture
def client():
    return FiskalyClient(api_key="test", api_secret="test")

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_authenticate_success(mock_request, client):
    # Simula respuesta exitosa de autenticación
    mock_request.return_value = {
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

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_authenticate_fail(mock_request, client):
    # Simula error de autenticación lanzando FiskalyAuthError
    mock_request.side_effect = FiskalyAuthError("Unauthorized")
    with pytest.raises(FiskalyAuthError):
        client.authenticate()

# tests/test_clients.py

from unittest.mock import patch
from fiskaly_sdk.models.client import ClientResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_clients_create(mock_request, client):
    mock_request.return_value = {
        "content": {"id": "client-id-1", "state": "ENABLED"}
    }
    resp = client.clients.create(client_id="client-id-1")
    assert isinstance(resp.content, ClientResponseContent)
    assert resp.content.id == "client-id-1"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_clients_list(mock_request, client):
    mock_request.return_value = {
        "content": [
            {"id": "client-id-1", "state": "ENABLED"},
            {"id": "client-id-2", "state": "DISABLED"},
        ]
    }
    resp_list = client.clients.list()
    assert len(resp_list) == 2
    assert resp_list[1].content.id == "client-id-2"

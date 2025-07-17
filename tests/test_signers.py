# tests/test_signers.py

from unittest.mock import patch
from fiskaly_sdk.models.signer import SignerResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_signers_create(mock_request, client):
    mock_request.return_value = {
        "content": {
            "id": "signer-id-1",
            "state": "ENABLED"
        }
    }
    resp = client.signers.create(signer_id="signer-id-1")
    assert isinstance(resp.content, SignerResponseContent)
    assert resp.content.id == "signer-id-1"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_signers_list(mock_request, client):
    mock_request.return_value = {
        "content": [
            {"id": "signer-id-1", "state": "ENABLED"},
            {"id": "signer-id-2", "state": "DISABLED"},
        ]
    }
    resp_list = client.signers.list()
    assert len(resp_list) == 2
    assert resp_list[0].content.id == "signer-id-1"

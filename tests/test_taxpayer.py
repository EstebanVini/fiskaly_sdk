# tests/test_taxpayer.py

from unittest.mock import patch
from fiskaly_sdk.models.taxpayer import TaxpayerResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_taxpayer_set(mock_request, client):
    mock_request.return_value = {
        "content": {
            "issuer": {"tax_number": "123", "legal_name": "Demo S.A."},
            "territory": "GIPUZKOA",
            "state": "ENABLED"
        }
    }
    resp = client.taxpayer.set("123", "Demo S.A.", "GIPUZKOA")
    assert isinstance(resp.content, TaxpayerResponseContent)
    assert resp.content.issuer.tax_number == "123"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_taxpayer_get(mock_request, client):
    mock_request.return_value = {
        "content": {
            "issuer": {"tax_number": "123", "legal_name": "Demo S.A."},
            "territory": "GIPUZKOA",
            "state": "ENABLED"
        }
    }
    resp = client.taxpayer.get()
    assert resp.content.issuer.legal_name == "Demo S.A."

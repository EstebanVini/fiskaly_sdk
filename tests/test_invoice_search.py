from unittest.mock import patch
from fiskaly_sdk.models.invoice import InvoiceResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_invoice_search_global(mock_request, client):
    mock_request.return_value = {
        "content": [
            {"id": "inv1", "state": "ISSUED"},
            {"id": "inv2", "state": "CANCELLED"},
        ]
    }
    resp = client.invoice_search.search(params={"from_date": "2024-01-01"})
    assert isinstance(resp[0].content, InvoiceResponseContent)

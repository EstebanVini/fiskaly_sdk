from unittest.mock import patch
from fiskaly_sdk.models.software import SoftwareResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_software_get(mock_request, client):
    mock_request.return_value = {
        "content": {"software_id": "soft123", "name": "DemoSoft"}
    }
    resp = client.software.get()
    assert isinstance(resp.content, SoftwareResponseContent)
    assert resp.content.name == "DemoSoft"

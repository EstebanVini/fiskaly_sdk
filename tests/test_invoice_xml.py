from unittest.mock import patch

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_invoice_xml_get(mock_request, client):
    mock_request.return_value = b"<xml>Factura</xml>"
    xml_bytes = client.invoice_xml.get_xml("client1", "inv123")
    assert xml_bytes.startswith(b"<xml>")

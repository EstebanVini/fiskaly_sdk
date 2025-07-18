# tests/test_exports.py

from unittest.mock import patch
from fiskaly_sdk.models.export import ExportResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_export_create(mock_request, client):
    mock_request.return_value = {
        "content": {"id": "export-id-1", "state": "RUNNING"}
    }
    resp = client.exports.create(export_id="export-id-1", content={})
    assert isinstance(resp.content, ExportResponseContent)
    assert resp.content.id == "export-id-1"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_export_download_zip(mock_request, client):
    # Devuelve bytes simulados (archivo ZIP)
    mock_request.return_value = b"Fake ZIP bytes"
    zip_bytes = client.exports.download_zip("export-id-1")
    assert isinstance(zip_bytes, bytes)
    assert zip_bytes == b"Fake ZIP bytes"

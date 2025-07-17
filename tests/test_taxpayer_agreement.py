from unittest.mock import patch

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_generate_agreement(mock_request, client):
    mock_request.return_value = {
        "content": {"agreement_id": "ag-123", "state": "DRAFT"}
    }
    resp = client.taxpayer_agreement.generate(content={"language": "es"})
    assert resp.content.agreement_id == "ag-123"
    assert resp.content.state == "DRAFT"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_upload_agreement(mock_request, client):
    mock_request.return_value = {
        "content": {"agreement_id": "ag-123", "state": "SIGNED"}
    }
    resp = client.taxpayer_agreement.upload(content={"file": "<base64>", "filename": "file.pdf"})
    assert resp.content.state == "SIGNED"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_download_pdf(mock_request, client):
    mock_request.return_value = b"%PDF-1.4 Fake"
    pdf_bytes = client.taxpayer_agreement.download_pdf()
    assert pdf_bytes.startswith(b"%PDF")

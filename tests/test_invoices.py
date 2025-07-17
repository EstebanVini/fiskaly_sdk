from unittest.mock import patch
from fiskaly_sdk.models.invoice import InvoiceResponseContent

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_enrichment_invoice(mock_request, client):
    mock_request.return_value = {
        "content": {"id": "enrich-id-1", "state": "ENRICHED"}
    }
    resp = client.invoices.enrichment_invoice(client_id="client1", content={"foo": "bar"})
    assert resp.content.id == "enrich-id-1"
    assert resp.content.state == "ENRICHED"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_correcting_invoice(mock_request, client):
    mock_request.return_value = {
        "content": {"id": "corr-id-1", "state": "CORRECTED"}
    }
    resp = client.invoices.correcting_invoice(client_id="client1", content={"original_invoice_id": "inv1"})
    assert resp.content.id == "corr-id-1"
    assert resp.content.state == "CORRECTED"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_remedy_invoice(mock_request, client):
    mock_request.return_value = {
        "content": {"id": "rem-id-1", "state": "REMEDIED"}
    }
    resp = client.invoices.remedy_invoice(client_id="client1", content={"reason": "recovery"})
    assert resp.content.id == "rem-id-1"
    assert resp.content.state == "REMEDIED"

@patch("fiskaly_sdk.client.FiskalyClient.request")
def test_vat_system_switch_invoice(mock_request, client):
    mock_request.return_value = {
        "content": {"id": "vat-id-1", "state": "SWITCHED"}
    }
    resp = client.invoices.vat_system_switch_invoice(client_id="client1", content={"vat_type": "special"})
    assert resp.content.id == "vat-id-1"
    assert resp.content.state == "SWITCHED"

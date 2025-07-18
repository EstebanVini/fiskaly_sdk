# fiskaly_sdk/api/invoice_xml.py

class InvoiceXMLAPI:
    """
    API para exportar una factura individual como XML.
    """
    def __init__(self, client):
        self.client = client

    def get_xml(self, client_id: str, invoice_id: str) -> bytes:
        """
        Descarga la factura en formato XML.
        """
        resp = self.client.request("GET", f"/clients/{client_id}/invoices/{invoice_id}/xml")
        return resp  # bytes

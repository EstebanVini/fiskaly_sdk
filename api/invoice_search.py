# fiskaly_sdk/api/invoice_search.py

from typing import Dict, Any, List
from ..models.invoice import InvoicesListResponse, InvoiceResponse

class InvoiceSearchAPI:
    """
    API para búsqueda global de facturas.
    """
    def __init__(self, client):
        self.client = client

    def search(self, params: Dict[str, Any]) -> List[InvoiceResponse]:
        """
        Busca facturas en toda la organización usando filtros globales.
        """
        resp = self.client.request("GET", "/invoices", params=params or {})
        list_response = InvoicesListResponse.parse_obj(resp)
        return [InvoiceResponse(content=item) for item in list_response.content]

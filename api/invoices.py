# fiskaly_sdk/api/invoices.py

"""
API para gestionar facturas (invoices) y casos especiales en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from ..exceptions import FiskalyApiError
from ..models.invoice import (
    InvoiceRequest,
    InvoiceResponse,
    InvoicesListResponse,
)
from ..utils import generate_guid

class InvoicesAPI:
    """
    API para gestionar facturas y casos avanzados (enrichment, correcting, remedy, VAT switch) en Fiskaly SIGN ES.
    """

    def __init__(self, client):
        self.client = client

    def create(self, client_id: str, invoice_id: Optional[str], content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Crea cualquier tipo de factura (SIMPLIFIED, COMPLETE, ENRICHMENT, CORRECTING, REMEDY, etc).

        :param client_id: ID del dispositivo emisor.
        :param invoice_id: ID único de la factura (si None, se genera uno nuevo).
        :param content: Cuerpo de la factura según especificación.
        :param metadata: Metadata adicional (opcional).
        :return: InvoiceResponse con los datos de la factura creada.
        """
        invoice_id = invoice_id or generate_guid()
        body = InvoiceRequest(content=content, metadata=metadata or {})
        resp = self.client.request("PUT", f"/clients/{client_id}/invoices/{invoice_id}", json=body.dict())
        return InvoiceResponse.model_validate(resp)

    def get(self, client_id: str, invoice_id: str) -> InvoiceResponse:
        """
        Recupera los datos de una factura específica.
        """
        resp = self.client.request("GET", f"/clients/{client_id}/invoices/{invoice_id}")
        return InvoiceResponse.model_validate(resp)

    def update_metadata(self, client_id: str, invoice_id: str, metadata: Dict[str, Any]) -> InvoiceResponse:
        """
        Actualiza la metadata de una factura.
        """
        body = {"content": {}, "metadata": metadata}
        resp = self.client.request("PATCH", f"/clients/{client_id}/invoices/{invoice_id}", json=body)
        return InvoiceResponse.model_validate(resp)

    def cancel(self, client_id: str, invoice_id: str, metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Cancela una factura (cambia estado a CANCELLED).
        """
        body = {"content": {"state": "CANCELLED"}, "metadata": metadata or {}}
        resp = self.client.request("PATCH", f"/clients/{client_id}/invoices/{invoice_id}", json=body)
        return InvoiceResponse.model_validate(resp)

    def list(self, client_id: str, params: Optional[Dict[str, Any]] = None) -> List[InvoiceResponse]:
        """
        Lista facturas para un client.
        """
        resp = self.client.request("GET", f"/clients/{client_id}/invoices", params=params or {})
        list_response = InvoicesListResponse.model_validate(resp)
        return [InvoiceResponse.model_validate({"content": item}) for item in list_response.content]

    # --- Helpers para casos especiales de facturación (opcional) ---
    # Estos métodos generan el payload adecuado y llaman a create().

    def create_enrichment_invoice(self, client_id: str, invoice_id: Optional[str], enrichment_content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Crea una factura de tipo ENRICHMENT.
        """
        content = {"type": "ENRICHMENT"}
        content.update(enrichment_content)
        return self.create(client_id, invoice_id, content, metadata)

    def create_correcting_invoice(self, client_id: str, invoice_id: Optional[str], correcting_content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Crea una factura rectificativa (CORRECTING).
        """
        content = {"type": "CORRECTING"}
        content.update(correcting_content)
        return self.create(client_id, invoice_id, content, metadata)

    def create_remedy_invoice(self, client_id: str, invoice_id: Optional[str], remedy_content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Crea una factura de recuperación (REMEDY).
        """
        content = {"type": "REMEDY"}
        content.update(remedy_content)
        return self.create(client_id, invoice_id, content, metadata)

    def create_vat_system_switch_invoice(self, client_id: str, invoice_id: Optional[str], vat_content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Crea una factura de cambio de sistema de IVA (VAT SYSTEM SWITCH).
        """
        content = {"type": "COMPLETE"}
        content.update(vat_content)
        return self.create(client_id, invoice_id, content, metadata)

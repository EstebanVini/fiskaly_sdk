# fiskaly_sdk/api/invoices.py

"""
API para gestionar facturas (invoices) y casos especiales (additional invoicing) 
en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from ..exceptions import FiskalyApiError
from ..models.invoice import (
    InvoiceRequest,
    InvoiceUpdateRequest,
    InvoiceCancelRequest,
    InvoiceResponse,
    InvoicesListResponse,
    InvoiceExportRequest,
    AdditionalInvoicingRequest,
)
from ..utils import generate_guid

class InvoicesAPI:
    """
    API para gestionar facturas y casos avanzados (enrichment, correcting, remedy, VAT switch).

    Métodos principales:
      - create
      - get
      - update
      - cancel
      - search
      - export
      - enrichment_invoices
      - correcting_invoices
      - remedy_invoices
      - vat_system_switch_invoices
    """

    def __init__(self, client):
        """
        Inicializa el submódulo invoices.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def create(self, client_id: str, invoice_id: Optional[str], content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Crea una nueva factura asociada a un client/dispositivo.

        :param client_id: ID del dispositivo (client) emisor.
        :param invoice_id: ID único de la factura (si None, se genera uno nuevo).
        :param content: Cuerpo de la factura según especificación.
        :param metadata: Metadata adicional (opcional).
        :return: InvoiceResponse con los datos de la factura creada.
        :raises FiskalyApiError: Si la API responde con error.
        """
        invoice_id = invoice_id or generate_guid()
        body = InvoiceRequest(content=content, metadata=metadata or {})
        resp = self.client.request("PUT", f"/clients/{client_id}/invoices/{invoice_id}", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

    def update(self, client_id: str, invoice_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Actualiza una factura existente (PATCH).

        :param client_id: ID del dispositivo emisor.
        :param invoice_id: ID de la factura a actualizar.
        :param content: Campos a actualizar.
        :param metadata: Metadata adicional.
        :return: InvoiceResponse con los datos actualizados.
        """
        body = InvoiceUpdateRequest(content=content, metadata=metadata or {})
        resp = self.client.request("PATCH", f"/clients/{client_id}/invoices/{invoice_id}", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

    def get(self, client_id: str, invoice_id: str) -> InvoiceResponse:
        """
        Recupera los datos de una factura específica.

        :param client_id: ID del dispositivo emisor.
        :param invoice_id: ID de la factura.
        :return: InvoiceResponse con los datos de la factura.
        """
        resp = self.client.request("GET", f"/clients/{client_id}/invoices/{invoice_id}")
        return InvoiceResponse.parse_obj(resp)

    def cancel(self, client_id: str, invoice_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Cancela una factura.

        :param client_id: ID del dispositivo emisor.
        :param invoice_id: ID de la factura a cancelar.
        :param content: Información para cancelación (según especificación).
        :param metadata: Metadata adicional.
        :return: InvoiceResponse con el nuevo estado.
        """
        body = InvoiceCancelRequest(content=content, metadata=metadata or {})
        resp = self.client.request("PATCH", f"/clients/{client_id}/invoices/{invoice_id}/cancel", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

    def search(self, client_id: str, params: Optional[Dict[str, Any]] = None) -> List[InvoiceResponse]:
        """
        Busca o lista facturas para un client.

        :param client_id: ID del dispositivo emisor.
        :param params: Parámetros de filtro/búsqueda (opcional).
        :return: Lista de InvoiceResponse.
        """
        resp = self.client.request("GET", f"/clients/{client_id}/invoices", params=params or {})
        list_response = InvoicesListResponse.parse_obj(resp)
        return [InvoiceResponse(content=item) for item in list_response.content]

    def export(self, client_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> Any:
        """
        Exporta facturas para un client (puede devolver ZIP).

        :param client_id: ID del dispositivo emisor.
        :param content: Parámetros de exportación.
        :param metadata: Metadata adicional.
        :return: Bytes o dict según exportación.
        """
        body = InvoiceExportRequest(content=content, metadata=metadata or {})
        resp = self.client.request("POST", f"/clients/{client_id}/invoices/export", json=body.dict())
        return resp

    # --- Additional Invoicing Use Cases ---

    def enrichment_invoice(self, client_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Enrichment Invoice: permite añadir información adicional a una factura.
        POST /clients/{client_id}/invoices/enrichment

        :param client_id: ID del dispositivo emisor.
        :param content: Información para enrichment.
        :param metadata: Metadata adicional.
        :return: InvoiceResponse con los datos enriquecidos.
        """
        body = AdditionalInvoicingRequest(content=content, metadata=metadata or {})
        resp = self.client.request("POST", f"/clients/{client_id}/invoices/enrichment", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

    def correcting_invoice(self, client_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Correcting Invoice: crea una factura rectificativa.
        POST /clients/{client_id}/invoices/correcting

        :param client_id: ID del dispositivo emisor.
        :param content: Información para corrección.
        :param metadata: Metadata adicional.
        :return: InvoiceResponse con los datos de la factura rectificativa.
        """
        body = AdditionalInvoicingRequest(content=content, metadata=metadata or {})
        resp = self.client.request("POST", f"/clients/{client_id}/invoices/correcting", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

    def remedy_invoice(self, client_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        Remedy Invoice: crea una factura de recuperación.
        POST /clients/{client_id}/invoices/remedy

        :param client_id: ID del dispositivo emisor.
        :param content: Información para remedy.
        :param metadata: Metadata adicional.
        :return: InvoiceResponse con los datos de la factura remedy.
        """
        body = AdditionalInvoicingRequest(content=content, metadata=metadata or {})
        resp = self.client.request("POST", f"/clients/{client_id}/invoices/remedy", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

    def vat_system_switch_invoice(self, client_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> InvoiceResponse:
        """
        VAT System Switch Invoice: factura para cambio de sistema de IVA.
        POST /clients/{client_id}/invoices/vat-system-switch

        :param client_id: ID del dispositivo emisor.
        :param content: Información para el cambio de sistema de IVA.
        :param metadata: Metadata adicional.
        :return: InvoiceResponse con los datos de la factura generada.
        """
        body = AdditionalInvoicingRequest(content=content, metadata=metadata or {})
        resp = self.client.request("POST", f"/clients/{client_id}/invoices/vat-system-switch", json=body.dict())
        return InvoiceResponse.parse_obj(resp)

# fiskaly_sdk/models/invoice.py

"""
Modelos de datos para el recurso Invoices (facturas) y casos especiales en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class InvoiceRequestContent(BaseModel):
    """
    Modelo del contenido principal de una factura para creación o actualización.
    """
    # Este esquema es un ejemplo, deberías adaptarlo a tu modelo real de datos de factura.
    # Los campos comunes se deben definir según el OpenAPI o la colección Postman.
    invoice_number: str = Field(..., description="Número de factura")
    issue_date: str = Field(..., description="Fecha de emisión (YYYY-MM-DD)")
    # Agrega todos los campos requeridos por tu modelo de factura Fiskaly
    # Por ejemplo: total, taxes, items, etc.
    # Ejemplo:
    # total: float = Field(..., description="Importe total")
    # taxes: List[Dict[str, Any]] = Field(..., description="Impuestos")
    # items: List[Dict[str, Any]] = Field(..., description="Líneas de factura")
    # ...

class InvoiceRequest(BaseModel):
    """
    Modelo completo de request para creación de factura.
    """
    content: Dict[str, Any]  # Admite flexibilidad de esquema según OpenAPI.
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class InvoiceUpdateRequest(BaseModel):
    """
    Modelo para actualizar/corregir una factura.
    """
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class InvoiceCancelRequest(BaseModel):
    """
    Modelo para cancelar una factura.
    """
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class InvoiceResponseContent(BaseModel):
    """
    Modelo para el contenido de la respuesta de una factura.
    """
    id: str = Field(..., description="ID único de la factura")
    state: Optional[str]
    # Agrega más campos según la respuesta de la API

class InvoiceResponse(BaseModel):
    """
    Modelo de respuesta para operaciones sobre una factura.
    """
    content: InvoiceResponseContent
    metadata: Optional[Dict[str, Any]] = None

class InvoicesListResponse(BaseModel):
    """
    Modelo para la respuesta de búsqueda/listado de facturas.
    """
    content: List[InvoiceResponseContent]

class InvoiceExportRequest(BaseModel):
    """
    Modelo para la solicitud de exportación de facturas.
    """
    content: Dict[str, Any]  # Parametros de filtro para exportación
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class AdditionalInvoicingRequest(BaseModel):
    """
    Modelo flexible para los endpoints de enrichment/correcting/remedy/vat-switch invoices.
    """
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

# fiskaly_sdk/models/invoice.py

"""
Modelos de datos para el recurso Invoices (facturas) y casos especiales en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class InvoiceRequest(BaseModel):
    """
    Modelo completo de request para creación de factura.
    El content es flexible para soportar todos los tipos: SIMPLIFIED, COMPLETE, ENRICHMENT, CORRECTING, REMEDY, etc.
    """
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class InvoiceResponseContent(BaseModel):
    """
    Modelo para el contenido de la respuesta de una factura.
    """
    id: str = Field(..., description="ID único de la factura")
    state: Optional[str]
    # Puedes agregar más campos según la respuesta de la API (ver OpenAPI o ejemplos reales)

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
    content: List[Dict[str, Any]]  # Cada item es un dict, se convertirá a InvoiceResponseContent en los métodos


# fiskaly_sdk/models/signer.py

"""
Modelos de datos para el recurso Signers en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class SignerRequestContent(BaseModel):
    """
    Modelo para el contenido requerido al crear/actualizar un signer.
    """
    # El API permite un body vacío o solo metadata, pero puede crecer en el futuro.
    pass

class SignerRequest(BaseModel):
    """
    Modelo completo para requests de creación/actualización de signer.
    """
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class SignerStateRequest(BaseModel):
    """
    Modelo para deshabilitar (PATCH) un signer.
    """
    content: Dict[str, str] = Field(..., description="Estado a establecer, p.ej: {'state': 'DISABLED'}")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class SignerResponseContent(BaseModel):
    """
    Contenido de la respuesta al obtener datos de un signer.
    """
    id: str = Field(..., description="ID del signer")
    state: Optional[str]
    # Puedes agregar otros campos según la respuesta completa de la API.

class SignerResponse(BaseModel):
    """
    Modelo completo de response para signer.
    """
    content: SignerResponseContent
    metadata: Optional[Dict[str, Any]] = None

class SignersListResponse(BaseModel):
    """
    Modelo para listar todos los signers.
    """
    content: list[SignerResponseContent]

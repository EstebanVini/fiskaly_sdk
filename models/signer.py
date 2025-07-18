# fiskaly_sdk/models/signer.py

"""
Modelos de datos para el recurso Signers en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

# -------- Certificado --------
class CertificateModel(BaseModel):
    expires_at: str = Field(..., description="Fecha de expiración del certificado")
    serial_number: str = Field(..., description="Número de serie del certificado")
    x509_pem: str = Field(..., description="Certificado X509 PEM")

# -------- Signer --------
class SignerContentModel(BaseModel):
    certificate: CertificateModel = Field(..., description="Datos del certificado")
    id: str = Field(..., description="ID del signer")
    state: str = Field(..., description="Estado del signer (ENABLED, DISABLED)")

class SignerModel(BaseModel):
    content: SignerContentModel
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

# -------- Request: Crear/Actualizar --------
class SignerRequestContent(BaseModel):
    # Si el API acepta body vacío o solo metadata, puedes dejarlo así.
    pass

class SignerRequest(BaseModel):
    content: Optional[Dict[str, Any]] = Field(default_factory=dict)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class SignerStateRequest(BaseModel):
    content: Dict[str, str] = Field(..., description="Estado a establecer, p.ej: {'state': 'DISABLED'}")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

# -------- Response: Uno solo --------
class SignerResponse(BaseModel):
    content: SignerContentModel
    metadata: Optional[Dict[str, Any]] = None

# -------- Response: Lista + paginación --------
class PaginationModel(BaseModel):
    limit: int = Field(..., description="Límite de resultados")
    next: Optional[str] = Field(None, description="URL del siguiente page")
    token: Optional[str] = Field(None, description="Token de paginación")

class SignersListResponse(BaseModel):
    pagination: PaginationModel
    results: List[SignerModel]

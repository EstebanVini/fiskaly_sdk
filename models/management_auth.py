# fiskaly_sdk/models/management_auth.py

"""
Modelos de datos para la autenticación en el SDK Fiskaly SIGN ES.
"""

from pydantic import BaseModel, Field

class ManagementAuthRequest(BaseModel):
    """
    Modelo de request completo para autenticación.
    """
    api_key: str = Field(..., description="API Key proporcionada por Fiskaly")
    api_secret: str = Field(..., description="API Secret proporcionado por Fiskaly")

class AccessTokenClaims(BaseModel):
    """
    Modelo para los claims del access token.
    """
    env: str = Field(..., description="Entorno de la autenticación (ej. TEST)")
    organization_id: str = Field(..., description="ID de la organización")

class ManagementAuthResponse(BaseModel):
    """
    Modelo de respuesta completa para autenticación.
    """
    access_token: str = Field(..., description="Token de acceso Bearer")
    access_token_claims: AccessTokenClaims = Field(..., description="Claims del access token")
    access_token_expires_in: int = Field(..., description="Segundos hasta la expiración del access token")
    access_token_expires_at: int = Field(..., description="Timestamp de expiración del access token")
    refresh_token: str = Field(..., description="Token de refresco")
    refresh_token_expires_in: int = Field(..., description="Segundos hasta la expiración del refresh token")
    refresh_token_expires_at: int = Field(..., description="Timestamp de expiración del refresh token")

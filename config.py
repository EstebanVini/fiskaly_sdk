# fiskaly_sdk/config.py

"""
Módulo de configuración del SDK Fiskaly.
"""

from dataclasses import dataclass
from typing import Optional 

@dataclass
class FiskalyConfig:
    """
    Almacena la configuración global del SDK Fiskaly SIGN ES.
    """
    api_key: str
    api_secret: str
    base_url: str = "https://sign-api.fiskaly.com/api/v1"

    timeout: int = 30
    organization_id: Optional[str] = None
    management_api_key: Optional[str] = None
    management_api_secret: Optional[str] = None

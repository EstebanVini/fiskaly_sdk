# fiskaly_sdk/config.py

"""
Módulo de configuración del SDK Fiskaly.
"""

from dataclasses import dataclass

@dataclass
class FiskalyConfig:
    """
    Almacena la configuración global del SDK Fiskaly SIGN ES.
    """
    api_key: str
    api_secret: str
    base_url: str = "https://sign-api.fiskaly.com/api/v1"
    timeout: int = 30

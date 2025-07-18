# fiskaly_sdk/client.py

"""
Módulo principal del SDK Fiskaly SIGN ES.
Contiene la clase FiskalyClient, punto de entrada para toda la funcionalidad.
"""

import requests
from typing import Optional, Dict, Any
from .config import FiskalyConfig
from .exceptions import (
    FiskalyApiError,
    FiskalyAuthError,
)
from .api.auth import AuthAPI
from .api.taxpayer import TaxpayerAPI
from .api.signers import SignersAPI
from .api.clients import ClientsAPI
from .api.invoices import InvoicesAPI
from .api.exports import ExportsAPI
from .api.taxpayer_agreement import TaxpayerAgreementAPI
from .api.invoice_xml import InvoiceXMLAPI
from .api.invoice_search import InvoiceSearchAPI
from .api.software import SoftwareAPI

class FiskalyClient:
    """
    Cliente principal para interactuar con la API de Fiskaly SIGN ES.
    Proporciona acceso a todos los recursos del API, maneja autenticación y configuración.
    """

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str = "https://sign-api.fiskaly.com/api/v1",
        timeout: int = 30,
        verify_ssl: bool = True
    ):
        self.config = FiskalyConfig(
            api_key=api_key,
            api_secret=api_secret,
            base_url=base_url,
            timeout=timeout
        )
        self.session = requests.Session()
        self._bearer_token: Optional[str] = None

        # Inicializa los recursos principales del API
        self.auth = AuthAPI(self)
        self.taxpayer = TaxpayerAPI(self)
        self.signers = SignersAPI(self)
        self.clients = ClientsAPI(self)
        self.invoices = InvoicesAPI(self)
        self.exports = ExportsAPI(self)
        self.taxpayer_agreement = TaxpayerAgreementAPI(self)
        self.invoice_xml = InvoiceXMLAPI(self)
        self.invoice_search = InvoiceSearchAPI(self)
        self.software = SoftwareAPI(self)
        self.verify_ssl = verify_ssl

    def authenticate(self) -> str:
        """
        Realiza la autenticación y obtiene un token Bearer.
        """
        token = self.auth.retrieve_access_token()
        self._bearer_token = token
        return token

    @property
    def headers(self) -> Dict[str, str]:
        """
        Obtiene los headers HTTP requeridos para las peticiones autenticadas.
        """
        if not self._bearer_token:
            raise FiskalyAuthError("El token Bearer no está presente. Llama a authenticate() primero.")
        return {
            "Authorization": f"Bearer {self._bearer_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.config.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
        # Para login: NO uses self.headers (que requiere Bearer)
        if endpoint == "/auth":
            # Solo content-type y accept
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                **headers
            }
        else:
            headers = {**self.headers, **headers}
        try:
            resp = self.session.request(
                method=method,
                url=url,
                headers=headers,
                timeout=self.config.timeout,
                verify=self.verify_ssl,
                **kwargs
            )
        except requests.RequestException as e:
            raise FiskalyApiError(f"Error en la conexión: {e}")

        if not resp.ok:
            try:
                err = resp.json()
            except Exception:
                err = resp.text
            raise FiskalyApiError(f"Error API [{resp.status_code}]: {err}")

        content_type = resp.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            return resp.json()
        else:
            return resp.content


    def set_bearer_token(self, token: str):
        self._bearer_token = token

    def get_bearer_token(self) -> Optional[str]:
        return self._bearer_token

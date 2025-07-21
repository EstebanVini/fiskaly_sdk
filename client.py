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
from .api.management_auth import ManagementAuthAPI
from .api.taxpayer import TaxpayerAPI
from .api.signers import SignersAPI
from .api.clients import ClientsAPI
from .api.invoices import InvoicesAPI
from .api.exports import ExportsAPI
from .api.taxpayer_agreement import TaxpayerAgreementAPI
from .api.invoice_xml import InvoiceXMLAPI
from .api.invoice_search import InvoiceSearchAPI
from .api.software import SoftwareAPI
from .api.organizations import OrganizationsAPI 

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
        management_api_key: Optional[str] = None,  # <-- Added parameter
        management_api_secret: Optional[str] = None,
        organization_id: Optional[str] = None,  # <-- Added parameter
    ):
        self.config = FiskalyConfig(
            api_key=api_key,
            api_secret=api_secret,
            base_url=base_url,
            timeout=timeout,
            organization_id=organization_id,
            management_api_key=management_api_key,
            management_api_secret=management_api_secret
        )
        self.session = requests.Session()
        self._bearer_token: Optional[str] = None
        #self._organization_id: Optional[str] = organization_id  # <-- Store organization_id
        self.management_bearer_token: Optional[str] = None

        # Set organization_id if provided
        if organization_id:
            self.config.organization_id = organization_id

        # Inicializa los recursos principales del API
        self.auth = AuthAPI(self)
        self.management_auth = ManagementAuthAPI(self)
        self.taxpayer = TaxpayerAPI(self)
        self.signers = SignersAPI(self)
        self.clients = ClientsAPI(self)
        self.invoices = InvoicesAPI(self)
        self.exports = ExportsAPI(self)
        self.taxpayer_agreement = TaxpayerAgreementAPI(self)
        self.invoice_xml = InvoiceXMLAPI(self)
        self.invoice_search = InvoiceSearchAPI(self)
        self.software = SoftwareAPI(self)
        self.organizations = OrganizationsAPI(self)


    def authenticate(self) -> str:
        """
        Realiza la autenticación y obtiene un token Bearer.
        """
        token = self.auth.retrieve_access_token()
        self._bearer_token = token
        return token
    
    def management_authenticate(self) -> str:
        """
        Realiza la autenticación administrativa y obtiene un token Bearer.
        """
        management_token, organization_id = self.management_auth.retrieve_management_access_token()
        self._bearer_token = management_token
        self.config.organization_id = organization_id
        return management_token , organization_id

    @property
    def headers(self) -> Dict[str, str]:
        """
        Obtiene los headers HTTP requeridos para las peticiones autenticadas.
        """
        if not self._bearer_token:
            raise FiskalyAuthError("El token Bearer no está presente. Llama a authenticate() primero.")
        headers = {
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
    
    def set_management_bearer_token(self, token: str):
        """
        Guarda el token Bearer para autenticación administrativa.
        """
        self.management_bearer_token = token

    def get_management_bearer_token(self) -> Optional[str]:
        """
        Obtiene el token Bearer para autenticación administrativa.
        """
        return self.management_bearer_token

    def set_organization_id(self, organization_id: str):
        """
        Guarda el ID de la organización en el cliente.
        """
        self.config.organization_id = organization_id

    def get_organization_id(self) -> Optional[str]:
        """
        Obtiene el ID de la organización configurado en el cliente.
        """
        return self.config.organization_id

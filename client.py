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

    Ejemplo de uso:
        client = FiskalyClient(
            api_key="tu_api_key",
            api_secret="tu_api_secret"
        )
        client.authenticate()
        info = client.taxpayer.get()
    """

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str = "https://sign-api.fiskaly.com/api/v1",
        timeout: int = 30,
    ):
        """
        Inicializa el cliente Fiskaly.

        :param api_key: API Key de tu cuenta Fiskaly.
        :param api_secret: API Secret de tu cuenta Fiskaly.
        :param base_url: URL base de la API SIGN ES (por defecto producción).
        :param timeout: Timeout para peticiones HTTP (segundos).
        """
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

    def authenticate(self) -> str:
        """
        Realiza la autenticación y obtiene un token Bearer.

        Este método debe ser llamado antes de acceder a cualquier recurso protegido.

        :return: Token Bearer obtenido.
        :raises FiskalyAuthError: Si falla la autenticación.
        """
        token = self.auth.retrieve_access_token()
        self._bearer_token = token
        return token

    @property
    def headers(self) -> Dict[str, str]:
        """
        Obtiene los headers HTTP requeridos para las peticiones autenticadas.

        :return: Diccionario con headers HTTP.
        :raises FiskalyAuthError: Si el token no ha sido inicializado.
        """
        if not self._bearer_token:
            raise FiskalyAuthError("El token Bearer no está presente. Llama a authenticate() primero.")
        return {
            "Authorization": f"Bearer {self._bearer_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def request(self, method: str, endpoint: str, **kwargs) -> Any:
        """
        Realiza una petición HTTP autenticada a la API Fiskaly.

        :param method: Método HTTP (GET, POST, PUT, PATCH, DELETE).
        :param endpoint: Path relativo del endpoint (ej: '/taxpayer').
        :param kwargs: Otros argumentos soportados por requests.request.
        :return: Respuesta decodificada (dict para JSON, bytes para binarios).
        :raises FiskalyApiError: Si la API responde con un error.
        """
        url = f"{self.config.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
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
        """
        Permite setear manualmente el token Bearer.

        Útil para flujos personalizados o restaurar sesiones.

        :param token: Token Bearer válido.
        """
        self._bearer_token = token

    def get_bearer_token(self) -> Optional[str]:
        """
        Obtiene el token Bearer actual.

        :return: Token Bearer, o None si no ha sido autenticado.
        """
        return self._bearer_token

# fiskaly_sdk/api/software.py

from ..models.software import SoftwareResponse

class SoftwareAPI:
    """
    API para consultar información de software registrado.
    """
    def __init__(self, client):
        self.client = client

    def get(self) -> SoftwareResponse:
        """
        Recupera la información del software registrado.
        """
        resp = self.client.request("GET", "/software")
        return SoftwareResponse.parse_obj(resp)

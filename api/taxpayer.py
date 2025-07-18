"""
API de Taxpayer: permite gestionar la información del contribuyente/emisor
en el SDK Fiskaly SIGN ES.
"""

from ..models.taxpayer import (
    TaxpayerRequest,
    TaxpayerResponse,
    TaxpayerStateRequest
)

class TaxpayerAPI:
    """
    API para gestionar el contribuyente/emisor ("taxpayer") en Fiskaly SIGN ES.
    Métodos disponibles:
      - set()       -> Crea o actualiza el taxpayer
      - get()       -> Recupera los datos actuales
      - disable()   -> Deshabilita (elimina lógicamente) el taxpayer
    """

    def __init__(self, client):
        """
        Inicializa el submódulo taxpayer.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def set(self, issuer_tax_number: str, issuer_legal_name: str, territory: str) -> TaxpayerResponse:
        """
        Crea o actualiza la información del taxpayer (emisor).

        :param issuer_tax_number: Número fiscal del emisor.
        :param issuer_legal_name: Nombre legal del emisor.
        :param territory: Territorio (ej: GIPUZKOA).
        :return: TaxpayerResponse con los datos actualizados.
        """
        body = TaxpayerRequest(
            content={
                "issuer": {
                    "tax_number": issuer_tax_number,
                    "legal_name": issuer_legal_name
                },
                "territory": territory
            }
        )
        resp = self.client.request("PUT", "/taxpayer", json=body.dict())
        return TaxpayerResponse.model_validate(resp)

    def get(self) -> TaxpayerResponse:
        """
        Recupera la información actual del taxpayer (emisor).

        :return: TaxpayerResponse con los datos actuales.
        """
        resp = self.client.request("GET", "/taxpayer")
        return TaxpayerResponse.model_validate(resp)

    def disable(self) -> TaxpayerResponse:
        """
        Deshabilita el taxpayer (emisor) de forma permanente.

        :return: TaxpayerResponse con el nuevo estado.
        """
        # El API requiere un body: {"content": {"state": "DISABLED"}}
        body = TaxpayerStateRequest(
            content={"state": "DISABLED"}
        )
        resp = self.client.request("PATCH", "/taxpayer", json=body.dict())
        return TaxpayerResponse.model_validate(resp)

# fiskaly_sdk/api/exports.py

"""
API para exportar facturas (exports) en el SDK Fiskaly SIGN ES.
Permite crear exportaciones, listar, obtener detalles, descargar ZIP y actualizar metadata.
"""

from typing import Optional, Dict, Any, List
from ..exceptions import FiskalyApiError
from ..models.export import (
    ExportRequest,
    ExportUpdateRequest,
    ExportResponse,
    ExportsListResponse,
)
from ..utils import generate_guid

class ExportsAPI:
    """
    API para gestionar exportaciones de facturas y la descarga de archivos ZIP de la exportación.

    Métodos principales:
      - create
      - get
      - list
      - download_zip
      - update_metadata
    """

    def __init__(self, client):
        """
        Inicializa el submódulo exports.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def create(self, export_id: Optional[str] = None, content: Dict[str, Any] = None, metadata: Optional[Dict[str, Any]] = None) -> ExportResponse:
        """
        Crea una nueva exportación de facturas.

        :param export_id: ID único de la exportación (si None, se genera uno nuevo).
        :param content: Filtros de exportación (según la API).
        :param metadata: Metadata adicional (opcional).
        :return: ExportResponse con los datos de la exportación creada.
        :raises FiskalyApiError: Si la API responde con error.
        """
        export_id = export_id or generate_guid()
        body = ExportRequest(content=content or {}, metadata=metadata or {})
        resp = self.client.request("PUT", f"/exports/{export_id}", json=body.dict())
        return ExportResponse.parse_obj(resp)

    def get(self, export_id: str) -> ExportResponse:
        """
        Recupera los datos de una exportación específica.

        :param export_id: ID de la exportación.
        :return: ExportResponse con los datos de la exportación.
        """
        resp = self.client.request("GET", f"/exports/{export_id}")
        return ExportResponse.parse_obj(resp)

    def list(self, params: Optional[Dict[str, Any]] = None) -> List[ExportResponse]:
        """
        Lista todas las exportaciones existentes.

        :param params: Parámetros de filtro para la búsqueda (opcional).
        :return: Lista de ExportResponse.
        """
        resp = self.client.request("GET", "/exports", params=params or {})
        list_response = ExportsListResponse.parse_obj(resp)
        return [ExportResponse(content=item) for item in list_response.content]

    def download_zip(self, export_id: str) -> bytes:
        """
        Descarga el archivo ZIP generado para una exportación.

        :param export_id: ID de la exportación.
        :return: Archivo ZIP en bytes (útil para guardar en disco).
        """
        resp = self.client.request("GET", f"/exports/{export_id}/file")
        return resp  # bytes

    def update_metadata(self, export_id: str, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> ExportResponse:
        """
        Actualiza la metadata de una exportación existente.

        :param export_id: ID de la exportación.
        :param content: Nueva metadata (dict).
        :param metadata: Metadata adicional.
        :return: ExportResponse con los datos actualizados.
        """
        body = ExportUpdateRequest(content=content, metadata=metadata or {})
        resp = self.client.request("PATCH", f"/exports/{export_id}", json=body.dict())
        return ExportResponse.parse_obj(resp)

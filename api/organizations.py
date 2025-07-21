import requests
from typing import Optional, Dict, Any
from ..models.organization import (
    Organization,
    ManagedOrganization,
    OrganizationResponse,
    ListOrganizationsResponse
)

class OrganizationsAPI:
    def __init__(self, client):
        self.client = client
        self.base_url = "https://dashboard.fiskaly.com/api/v0"
        try:
            # Asigna el organization_id del cliente a la configuración del cliente
            self.client.config.organization_id = client.config.organization_id
        except AttributeError:
            # Si no existe, crea un nuevo atributo organization_id en el cliente
            self.client.config.organization_id = None 

    def _get_headers(self) -> Dict[str, str]:
        # Asume que el token JWT está en self.client.access_token
        return {
            "Authorization": f"Bearer {self.client.management_bearer_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def list_organizations(self, params: Optional[Dict[str, Any]] = None) -> ListOrganizationsResponse:
        url = f"{self.base_url}/organizations"
        headers = self._get_headers()
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return ListOrganizationsResponse.model_validate(resp.json())

    def create_organization(self, org_data: Organization) -> OrganizationResponse:
        url = f"{self.base_url}/organizations"
        headers = self._get_headers()
        resp = requests.post(url, headers=headers, json=org_data.model_dump(exclude_none=True))
        resp.raise_for_status()
        return OrganizationResponse.model_validate(resp.json())

    def retrieve_organization(self, organization_id: str) -> OrganizationResponse:
        url = f"{self.base_url}/organizations/{organization_id}"
        headers = self._get_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return OrganizationResponse.model_validate(resp.json())

    def update_organization(self, organization_id: str, org_data: Dict[str, Any]) -> OrganizationResponse:
        url = f"{self.base_url}/organizations/{organization_id}"
        headers = self._get_headers()
        resp = requests.patch(url, headers=headers, json=org_data)
        resp.raise_for_status()
        return OrganizationResponse.model_validate(resp.json())

    def delete_organization(self, organization_id: str) -> Dict:
        url = f"{self.base_url}/organizations/{organization_id}"
        headers = self._get_headers()
        resp = requests.delete(url, headers=headers)
        resp.raise_for_status()
        return resp.json()

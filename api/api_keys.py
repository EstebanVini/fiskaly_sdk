import requests
from typing import Optional, Dict, Any
from ..models.api_key import ManagedApiKey, ApiKeyResponse, ListApiKeyResponse

class ApiKeysAPI:
    def __init__(self, client):
        self.client = client
        self.base_url = "https://dashboard.fiskaly.com/api/v0"

    def list_managed_api_keys(self, organization_id: str, params: Optional[Dict[str, Any]] = None) -> ListApiKeyResponse:
        url = f"{self.base_url}/organizations/{organization_id}/api-keys"
        headers = {
            "Authorization": f"Bearer {self.client.access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return ListApiKeyResponse.model_validate(resp.json())

    def create_managed_api_key(self, organization_id: str, api_key_data: ManagedApiKey) -> ApiKeyResponse:
        url = f"{self.base_url}/organizations/{organization_id}/api-keys"
        headers = {
            "Authorization": f"Bearer {self.client.access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.post(url, headers=headers, json=api_key_data.dict(exclude_none=True))
        resp.raise_for_status()
        result = ApiKeyResponse.model_validate(resp.json())
        # ¡Actualiza api_key y api_secret en el cliente!
        if hasattr(result, "key") and hasattr(result, "secret"):
            self.client.set_api_key_and_secret(result.key, result.secret)
        return result

    def retrieve_api_key(self, organization_id: str, api_key_id: str) -> ApiKeyResponse:
        url = f"{self.base_url}/organizations/{organization_id}/api-keys/{api_key_id}"
        headers = {
            "Authorization": f"Bearer {self.client.access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return ApiKeyResponse.model_validate(resp.json())

    def update_managed_api_key(self, organization_id: str, api_key_id: str, update_data: Dict[str, Any]) -> ApiKeyResponse:
        url = f"{self.base_url}/organizations/{organization_id}/api-keys/{api_key_id}"
        headers = {
            "Authorization": f"Bearer {self.client.access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.patch(url, headers=headers, json=update_data)
        resp.raise_for_status()
        result = ApiKeyResponse.model_validate(resp.json())
        # Si viene un secret (a veces solo viene al crear), lo actualiza en el client
        if hasattr(result, "key"):
            self.client.set_api_key_and_secret(result.key, getattr(result, "secret", None))
        return result

    def delete_managed_api_key(self, organization_id: str, api_key_id: str) -> Dict:
        url = f"{self.base_url}/organizations/{organization_id}/api-keys/{api_key_id}"
        headers = {
            "Authorization": f"Bearer {self.client.access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.delete(url, headers=headers)
        resp.raise_for_status()
        return resp.json()

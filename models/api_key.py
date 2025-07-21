from typing import Optional, Dict, List
from pydantic import BaseModel

class ManagedApiKey(BaseModel):
    name: str
    status: str  # "enabled" o "disabled"
    managed_by_organization_id: str
    metadata: Optional[Dict[str, str]] = None

class ApiKeyResponse(BaseModel):
    _id: str
    _type: str
    _envs: List[str]
    key: str
    created_at: int
    name: str
    status: str
    metadata: Optional[Dict[str, str]] = None
    secret: Optional[str] = None
    managed_by_organization_id: Optional[str] = None
    created_by_user: Optional[str] = None

class ListApiKeyResponse(BaseModel):
    data: List[ApiKeyResponse]
    count: int
    _type: str

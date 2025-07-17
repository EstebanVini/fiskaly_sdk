# tests/conftest.py

import pytest
from fiskaly_sdk.client import FiskalyClient

@pytest.fixture
def client():
    """
    Provee una instancia de FiskalyClient para los tests.
    """
    return FiskalyClient(
        api_key="test_api_key",
        api_secret="test_api_secret",
        base_url="https://sign-api.fiskaly.com/api/v1"
    )

# fiskaly_sdk/utils.py

"""
Utilidades varias para el SDK Fiskaly.
"""

import uuid

def generate_guid() -> str:
    """
    Genera un GUID (UUID4) válido para operaciones PUT en la API Fiskaly.
    
    :return: String UUID.
    """
    return str(uuid.uuid4())

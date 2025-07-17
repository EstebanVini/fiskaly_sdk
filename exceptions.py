# fiskaly_sdk/exceptions.py

"""
Excepciones propias del SDK Fiskaly SIGN ES.
"""

class FiskalyError(Exception):
    """
    Error base del SDK Fiskaly.
    """
    pass

class FiskalyApiError(FiskalyError):
    """
    Errores relacionados con la respuesta de la API Fiskaly.
    """
    pass

class FiskalyAuthError(FiskalyError):
    """
    Errores relacionados con autenticación.
    """
    pass

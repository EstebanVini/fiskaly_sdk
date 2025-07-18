# examples/error_handling.py

"""
Ejemplo de manejo de errores del SDK Fiskaly SIGN ES.
"""

from fiskaly_sdk import FiskalyClient
from fiskaly_sdk.exceptions import FiskalyApiError, FiskalyAuthError

client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)

try:
    client.authenticate()
    # Intentar obtener una factura que NO existe
    factura = client.invoices.get(client_id="client-fake", invoice_id="invoice-fake")
    print("Factura:", factura.content)
except FiskalyAuthError as e:
    print("Error de autenticación:", e)
except FiskalyApiError as e:
    print("Error de la API Fiskaly:", e)
except Exception as e:
    print("Error inesperado:", e)

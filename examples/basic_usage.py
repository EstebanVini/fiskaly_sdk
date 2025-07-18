# examples/basic_usage.py

"""
Ejemplo básico: autenticación y obtención de información de taxpayer.
"""

from fiskaly_sdk import FiskalyClient

# Instancia del cliente con credenciales (usa variables de entorno para prod)
client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)

# Autenticación
token = client.authenticate()
print("Bearer Token:", token)

# Obtener información del taxpayer (emisor)
taxpayer = client.taxpayer.get()
print("Taxpayer:", taxpayer.content)

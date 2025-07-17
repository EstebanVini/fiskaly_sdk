# examples/clients_usage.py

"""
Ejemplo de gestión de clients (dispositivos clientes/TPV) en el SDK Fiskaly SIGN ES.
"""

from fiskaly_sdk import FiskalyClient

client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)
client.authenticate()

# Crear un client (dispositivo)
client_resp = client.clients.create(metadata={"tpv": "TPV-Principal"})
print("Client creado:", client_resp.content)

# Listar todos los clients
clients_list = client.clients.list()
print("Clients en la organización:")
for c in clients_list:
    print(f"  - {c.content.id} (estado: {c.content.state})")

# Obtener datos de un client específico
client_id = client_resp.content.id
client_info = client.clients.get(client_id)
print("Info del client:", client_info.content)

# Deshabilitar un client
disable_resp = client.clients.disable(client_id)
print("Client deshabilitado:", disable_resp.content)

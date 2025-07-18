from fiskaly_sdk import FiskalyClient

client = FiskalyClient(api_key="...", api_secret="...")
client.authenticate()

software = client.software.get()
print("Software info:", software.content)

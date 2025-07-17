from fiskaly_sdk import FiskalyClient

client = FiskalyClient(api_key="...", api_secret="...")
client.authenticate()

result = client.invoice_search.search(params={"from_date": "2024-01-01", "to_date": "2024-07-01"})
for inv in result:
    print(inv.content)

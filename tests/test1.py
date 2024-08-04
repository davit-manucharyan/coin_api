import requests

headers = {
    'X-CMC_PRO_API_KEY': '0b3ca1c1-ebd8-4c09-87e9-ab8b90cff2d6'
          }

response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                        headers=headers)

response_json = response.json()

print(response_json.get('data')[0].get('total_supply'))

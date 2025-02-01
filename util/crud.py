import requests
import json
from icecream import ic



def makeRequestBit(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            return json.dumps(result)
        else:
            ic('Error:', response.status_code)
            return None
    except:
        ic("error")








# looks like this isn't how we receive finnhub_client as some obj gets printed
def makeRequest(finnhub_client):
    print(finnhub_client.stock_tick('AAPL', '2024-10-14', 500, 0))



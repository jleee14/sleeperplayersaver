import requests
import json

def api_request():
    API_URL = 'https://api.sleeper.app/v1/players/nfl'
    
    try:
        r = requests.get(API_URL)
        player_data = json.loads(r.content)
    
    except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as err:
        print(f"Error: {err}")

    with open('playerdata.json', 'w') as f:
        f.seek(0)
        json.dump(player_data, f, indent=4, sort_keys=True)

api_request()
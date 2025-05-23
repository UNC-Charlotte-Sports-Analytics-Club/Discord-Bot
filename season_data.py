import json
import requests 
import pandas as pd 
import numpy as np

url = "https://nfl-api-data.p.rapidapi.com/nfl-whitelist"
headers = {
	"x-rapidapi-key": "d38df622admsh3eb9f140630eeb1p1cc193jsn31584b95d649",
	"x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
data = response.json()

print(json.dumps(data, indent=2))

season_data = data.get("season_info", [])

df = pd.DataFrame(season_data)

print(df)



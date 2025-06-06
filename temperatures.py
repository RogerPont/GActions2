import requests
import json
from datetime import datetime

# Coordenades del poble/ciutat que vulguis (exemple: Barcelona)
latitude = 41.39
longitude = 2.16

# API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

# Crida a l'API
response = requests.get(url)
data = response.json()

temperatures = data["hourly"]["temperature_2m"]

# Calculs
temp_max = max(temperatures)
temp_min = min(temperatures)
temp_avg = sum(temperatures) / len(temperatures)

# Data actual
today = datetime.now().strftime("%Y%m%d")

# Resultat
output = {
    "date": today,
    "max_temperature": temp_max,
    "min_temperature": temp_min,
    "average_temperature": temp_avg
}

# Guardar a JSON
with open(f"temp_{today}.json", "w") as f:
    json.dump(output, f, indent=4)

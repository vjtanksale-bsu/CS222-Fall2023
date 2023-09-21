import json
import ssl
from urllib.request import urlopen

def CAAlert():
    url = "https://api.weather.gov/alerts/active?area=CA"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())
    return weatherData["features"][0]["properties"]["event"]

def main():
    state = input("Enter two-character state code: ")
    url = "https://api.weather.gov/alerts/active?area=" + state
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())
    for e in weatherData["features"]:
        print(e["properties"]["event"])
        print(e["properties"]["headline"])
        print(e["properties"]["description"])
        
main()
"""
Code challenge based on your learnings:

Write a Python script to get the current weather of a city inputted from the command line. Use the OpenWeatherMap API.

Use the requests module to download a webpage and save its content to a file.

Use sys.argv to accept user input from the command line and search for the input in a JSON file.

Use a for loop to iterate over a dictionary and print each key-value pair.
"""

import sys
import json
import requests

def main():
    if len(sys.argv)!=2:   # Exit if a city name wasn't provided as a command line argument
        sys.exit()
    find_city = requests.get("http://api.openweathermap.org/geo/1.0/direct?q="+sys.argv[1]+"&limit=5&appid=88afa02aa51073d5799354d2a8415e3d")
    cities = (json.dumps(find_city.json(), indent=2))
    #print(london) test that the london stored data
    for city in cities:

        
main()

"""
if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={88afa02aa51073d5799354d2a8415e3d}")
print(response.json)

"""

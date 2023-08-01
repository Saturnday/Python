"""
Code challenge based on your learnings:

Write a Python script to get the current weather of a city inputted from the command line. Use the OpenWeatherMap API.

Use the requests module to download a webpage and save its content to a file.

Use sys.argv to accept user input from the command line and search for the input in a JSON file.

Use a for loop to iterate over a dictionary and print each key-value pair.
"""
"""

all usless!!! doesn't work without subscribtion,401 error

"""
import sys
import json
import requests

def main():
    if len(sys.argv)!=2:   # Exit if a city name wasn't provided as a command line argument
        sys.exit()
    find_city = requests.get("http://api.openweathermap.org/geo/1.0/direct?q="+sys.argv[1]+"&limit=5&appid=88afa02aa51073d5799354d2a8415e3d")
    i = find_city.json()
    if i:
        latitude = i[0]['lat']
        longitude = i[0]['lon']
        thecity=requests.get("https://api.openweathermap.org/data/3.0/onecall?lat="+str(latitude)+"&lon="+str(longitude)+"&appid=88afa02aa51073d5799354d2a8415e3d")
        thecity=thecity.json
        print(latitude)
        print(longitude)
        print(thecity)
        #print("the weather of the"+sys.argv[1]+"is"+str(thecity))

        
main()

"""
if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={88afa02aa51073d5799354d2a8415e3d}")
print(response.json)

"""

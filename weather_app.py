import requests
API_KEY = "7fd852cf83203343a16c18d71e34e9c4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        url = BASE_URL + "?q=" + city + "&appid=" + API_KEY + "&units=imperial"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            name = data["name"]
            temp = data["main"]["temp"]
            feels = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            print("")
            print("="*30)
            print("  Weather in " + name)
            print("="*30)
            print("condition: " + condition)
            print("temperature: " + str(round(temp)) + "°F")
            print("feels like: " + str(round(feels)) + "°F")
            print("humidity: " + str(humidity) + "%")
        else:
            print("City not found. Please check Earth city name and try again.")
    except Exception as e:
        print("Error: " + str(e))

city = input("Enter a city name to get the current weather: ")
get_weather(city)

while True:
    city = input("Enter another city name to get the current weather (or type 'exit' to quit): ")
    if city.lower() == "exit":
        print ("Dueces")
        break
    get_weather(city)
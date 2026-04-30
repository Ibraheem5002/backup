import requests
import geocoder

def get_lat_lon():
    g = geocoder.ip('me')
    if g.ok:
        dic = {
            "lat" : g.latlng[0],
            "lon" : g.latlng[1]
        }
        return dic
    else:
        return None

def get_current_weather():
    location = get_lat_lon()

    if location == None:
        print("ERROR: unable to get location")
        return None
    else:
        lat = location['lat']
        lon = location['lon']

        apiKey = "bf3f1165b1dc2160b9321af4268bc660"
        apiURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"

        response = requests.get(apiURL)
        
        if response.status_code != 200:
            print("ERROR: cannot fetch the weather api")
            return None
        else:
            apiData = response.json()
            main = apiData['weather'][0]['main']
            temp = apiData['main']['temp']
            temp = round(temp-273.15,2)
            dic = {
                "main" : main,
                "temp" : temp
            }
            return dic

def get_city_weather(city):
    apiKey = "bf3f1165b1dc2160b9321af4268bc660"
    apiURL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"

    response = requests.get(apiURL)

    if response.status_code != 200:
        print("ERROR: cannot fetch the weather api")
        return None
    else:
        apiData = response.json()
        main = apiData['weather'][0]['main']
        temp = apiData['main']['temp']
        dic = {
            "main" : main,
            "temp" : temp
        }
        return dic

# print(get_current_weather())
# print(get_lat_lon())
# print(get_city_weather("karachi"))
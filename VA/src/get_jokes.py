import requests

apiURL = "https://v2.jokeapi.dev/joke/Any?type=single"


def getJoke():
    response = requests.get(apiURL)

    if response.status_code != 200:
        print("ERROR: error in fetching jokes api")
        return None
    else:
        apiData = response.json()
        return apiData['joke']

# joke = getJoke()
# print(joke)
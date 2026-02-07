import requests

def fetch_weather(city: str, api_key: str) ->dict:
    """
    Fetch weather data from open weather api
    """
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q' : city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(url, params= params, timeout= 30)
    if response.status_code != 200:
        raise Exception(f'weather Api failed| status: {response.status_code}| Response: {response.text}')
    return response.json()
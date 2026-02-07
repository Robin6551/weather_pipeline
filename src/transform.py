from datetime import datetime

def transform_weather_data(raw_data: dict) -> tuple[dict, dict]:
    """
    Transforms raw weather API Json into:
    dim_location recode
    fact_weather recode
    """

    dim_location = {
        'city': raw_data['name'],
        'country': raw_data['sys']['country'],
        'latitude': raw_data['coord']['lat'],
        'longitude': raw_data['coord']['lon'],
    }

    fact_weather = {
        'observed_at': datetime.utcfromtimestamp(raw_data['dt']),
        'temperature': raw_data['main']['temp'],
        "humidity": raw_data["main"]["humidity"],
        "pressure": raw_data["main"]["pressure"],
        "weather_main": raw_data["weather"][0]["main"],
        "weather_description": raw_data["weather"][0]["description"],
    }

    return dim_location, fact_weather



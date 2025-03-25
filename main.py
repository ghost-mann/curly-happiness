from src.extract import get_weather_data
from src.transform import clean_weather_data
from src.load import save_to_database


def main():

    API_KEY = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/nairobi?unitGroup=us&key=YOUR_API_KEY&contentType=json'
    CITY = 'Nairobi'

    # Extract
    raw_data = get_weather_data(CITY, API_KEY)

    # Transform
    cleaned_data = clean_weather_data(raw_data)

    # Load
    if cleaned_data:
        save_to_database(cleaned_data)
    else:
        print("No data to save")


if __name__ == '__main__':
    main()
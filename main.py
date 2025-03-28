from extract import get_weather_data
from transform import clean_weather_data
from load import save_to_database


def main():

    API_KEY = 'aadbb980690277918b13cd7721aa3d06'
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
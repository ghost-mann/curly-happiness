def clean_weather_data(raw_data):
    """Clean and extract useful information from raw weather data"""
    if not raw_data:
        return None

    return {
        'city': raw_data['name'],
        'temperature': raw_data['main']['temp'] - 273.15,  # Convert Kelvin to Celsius
        'humidity': raw_data['main']['humidity'],
        'description': raw_data['weather'][0]['description']
    }
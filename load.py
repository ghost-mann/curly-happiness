import sqlite3


def save_to_database(weather_data):
    """Save weather data to a SQLite database"""
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            description TEXT
        )
    ''')

    # Insert data
    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, description)
        VALUES (?, ?, ?, ?)
    ''', (
        weather_data['city'],
        weather_data['temperature'],
        weather_data['humidity'],
        weather_data['description']
    ))

    conn.commit()
    conn.close()
    print("Data saved successfully!")
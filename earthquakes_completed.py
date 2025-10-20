# Completed earthquake data analysis code
# Based on original earthquakes.py file, filled in all missing functions

import requests
import json
from datetime import datetime

def get_data():
    """
    Get earthquake data from USGS and parse into Python object
    """
    # Use requests library to get data
    response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
        params={
            'starttime': "2000-01-01",
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
            "minmagnitude": "1",
            "endtime": "2018-10-11",
            "orderby": "time-asc"
        }
    )

    # Get response text
    text = response.text
    
    # Parse JSON text into Python object
    data = json.loads(text)
    return data

def count_earthquakes(data):
    """Get total number of earthquakes"""
    return len(data['features'])

def get_magnitude(earthquake):
    """Get earthquake magnitude"""
    return earthquake['properties']['mag']

def get_location(earthquake):
    """Get earthquake location (latitude and longitude)"""
    coordinates = earthquake['geometry']['coordinates']
    # Return latitude and longitude (ignore altitude)
    return coordinates[1], coordinates[0]  # 纬度, 经度

def get_maximum(data):
    """Find the magnitude and location of the strongest earthquake"""
    max_magnitude = 0
    max_location = (None, None)
    
    for earthquake in data['features']:
        magnitude = get_magnitude(earthquake)
        if magnitude and magnitude > max_magnitude:
            max_magnitude = magnitude
            max_location = get_location(earthquake)
    
    return max_magnitude, max_location

# Main program execution
if __name__ == "__main__":
    print("Fetching earthquake data...")
    data = get_data()
    
    print(f"Loaded {count_earthquakes(data)} earthquake events")
    
    max_magnitude, max_location = get_maximum(data)
    print(f"Strongest earthquake located at {max_location} with magnitude {max_magnitude}")

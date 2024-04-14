import requests
import os
from dotenv import load_dotenv
from helper_functions import *
import argparse

load_dotenv()

# Strava API endpoint for activities
URL = "https://www.strava.com/api/v3/athlete/activities"

def setup_api_call():

    # get access token from .env file
    access_token = os.getenv("ACCESS_TOKEN")

    # Headers to include with our request
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    return headers


def main(activity_type, start_time, end_time):

    headers = setup_api_call()

    end_time = datetime_to_unix_timestamp(end_time)
    start_time = datetime_to_unix_timestamp(start_time)

    # Parameters for the request
    params = {
        'before': datetime_to_unix_timestamp(end_time),
        'after': datetime_to_unix_timestamp(start_time),
        'per_page': 200,  # Adjust based on how many activities you expect to retrieve
        'page': 1,  # Use pagination to retrieve more activities
    }

    # Make the GET request to Strava API
    response = requests.get(URL, headers=headers, params=params)


    # Check if the request was successful
    if response.status_code == 200:
        activities = response.json()
        cycling_activities = [activity for activity in activities if activity['type'] == activity_type]
        for activity in cycling_activities:
            print(f"Activity ID: {activity['id']} - Name: {activity['name']}")
    else:
        print(f"Error fetching activities. Status Code: {response.status_code}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Query Strava activities by type and date range.')
    parser.add_argument('activity_type', type=str, help='Type of activity (e.g., "Ride", "Run", "VirtualRide)')
    parser.add_argument('start_time', type=str, help='Start date in YYYY-MM-DD format')
    parser.add_argument('end_time', type=str, help='End date in YYYY-MM-DD format')

    args = parser.parse_args()

    main(args.activity_type, args.start_time, args.end_time)
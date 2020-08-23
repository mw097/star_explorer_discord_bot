import settings
import requests
from datetime import date


class NASAClient:

    def fetch_apod_img(self, imgDate: str = 'Today'):
        """Fetch the Astronomy Photo of Day"""

        URL_APOD = "https://api.nasa.gov/planetary/apod"
        params = {
            'api_key': settings.key_nasa,
            'date': date.today().strftime("%Y-%m-%d") if imgDate == 'Today' else imgDate,
            'hd': 'True' if settings.apod_quality_hd else 'False'
        }
        response = requests.get(URL_APOD, params=params).json()

        if settings.apod_quality_hd:
            return response['hdurl']
        else:
            return response['url']

    def fetch_neows_feed_count(self, dates):
        """Retrieve a list of asteroids based on their closes approach date to Earth"""

        URL_NEOWSFEED = "https://api.nasa.gov/neo/rest/v1/feed"
        params = {
            'api_key': settings.key_nasa,
            'start_date': dates[0],
            'end_date': dates[1]
        }
        response = requests.get(URL_NEOWSFEED, params=params).json()

        return response['element_count']

    def fetch_neows_feed_list(self, dates):
        """Retrieve a list of asteroids based on their closes approach date to Earth"""

        URL_NEOWSFEED = "https://api.nasa.gov/neo/rest/v1/feed"
        params = {
            'api_key': settings.key_nasa,
            'start_date': dates[0],
            'end_date': dates[1]
        }
        response = requests.get(URL_NEOWSFEED, params=params).json()
        asteroids = []

        for day in response['near_earth_objects'].values():
            for asteroid in day:
                asteroids.append('ID: ' + asteroid['id']  + ', URL: ' + asteroid['nasa_jpl_url'])

        return asteroids

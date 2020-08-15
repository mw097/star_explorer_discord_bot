import settings
import requests
from urllib.request import urlretrieve
from datetime import date


class NASAClient:
    def fetch_apod_img(self):
        """Fetch Astronomy Photo of Day"""

        URL_APOD = "https://api.nasa.gov/planetary/apod"
        params = {
            'api_key': settings.key_nasa,
            'date': date.today().strftime("%Y-%m-%d"),
            'hd': 'True' if settings.apod_quality_hd else 'False'
        }
        response = requests.get(URL_APOD, params=params).json()

        if settings.apod_quality_hd:
            return response['hdurl']
        else:
            return response['url']
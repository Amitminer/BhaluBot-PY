import requests
from typing import Optional
from .ConfigManager import ConfigManager

class ImageManager:

    @staticmethod
    async def get_random_image(query: Optional[str] = None) -> Optional[str]:
        try:
            access_key = ConfigManager.get_unsplash_key()
            if not access_key:
                return "Error: API key is not provided. Please set up the API key in the configuration."

            params = {'client_id': access_key}
            if query:
                params['query'] = query

            response = requests.get("https://api.unsplash.com/photos/random", params=params)
            response.raise_for_status()

            data = response.json()
            image_url = data['urls']['regular']

            return image_url
        
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Unsplash API: {e}")
            return "Error: Failed to fetch a random image. Please try again later."
        
        except KeyError as e:
            print(f"Error parsing JSON response: {e}")
            return "Error: Unexpected response from the Unsplash API. Please try again later."
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            return "Error: An unexpected error occurred. Please try again later."
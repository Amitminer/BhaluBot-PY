import requests
from typing import Optional
from .ConfigManager import ConfigManager

class ImageManager:
    """
    Manages image-related operations, such as fetching random images from Unsplash.
    """

    @staticmethod
    async def get_image(query: Optional[str] = None) -> Optional[str]:
        """
        Get a random image from Unsplash.
        """
        try:
            access_key = ImageManager._get_access_key()
            if not access_key:
                return "Error: API key is not provided. Please set up the API key in the configuration."

            params = {'client_id': access_key}
            if query:
                params['query'] = query

            response = requests.get("https://api.unsplash.com/photos/random", params=params)
            response.raise_for_status()

            data = response.json()
            image_url = data.get('urls', {}).get('regular')

            if not image_url:
                return "Error: No image URL found in the response."

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

    @staticmethod
    def _get_access_key() -> Optional[str]:
        """
        Get the appropriate Unsplash access key based on configuration.
        """
        if ConfigManager.using_unsplash_key2():
            return ConfigManager.get_unsplash_key2()
        else:
            return ConfigManager.get_unsplash_key()

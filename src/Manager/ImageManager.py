import requests
from typing import Optional
from .ConfigManager import ConfigManager


class ImageManager:
    """
    Manages image-related operations, such as fetching random images from Unsplash.
    """

    unsplashApi_Url = "https://api.unsplash.com/photos/random"

    @staticmethod
    async def get_image(query: Optional[str] = None) -> Optional[str]:
        access_key = ImageManager._get_access_key()
        if not access_key:
            return ImageManager._handle_missing_access_key()

        params = {"client_id": access_key}
        if query:
            params["query"] = query

        response = ImageManager._make_request(params)
        if not response:
            return "Error: Failed to fetch a random image. Please try again later."

        image_url = ImageManager._extract_image_url(response)
        if not image_url:
            return "Error: No image URL found in the response."

        return image_url

    @staticmethod
    def _get_access_key() -> Optional[str]:
        if using_key2 := ConfigManager.using_unsplash_key2():
            return (
                ConfigManager.get_unsplash_key2()
                if using_key2
                else ConfigManager.get_unsplash_key()
            )
        return None

    @staticmethod
    def _handle_missing_access_key() -> str:
        return "Error: API key is not provided. Please set up the API key in the configuration."

    @staticmethod
    def _make_request(params: dict) -> Optional[requests.Response]:
        try:
            return requests.get(ImageManager.unsplashApi_Url, params=params)
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Unsplash API: {e}")
            return None

    @staticmethod
    def _extract_image_url(response: requests.Response) -> Optional[str]:
        try:
            data = response.json()
            return data.get("urls", {}).get("regular")
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
            return None

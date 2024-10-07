import aiohttp
import base64
import os
from typing import Optional, Dict, Any
from .ConfigManager import ConfigManager
from together import Together
import aiofiles
import asyncio
from aiohttp import ClientTimeout

class ImageManager:
    """
    Manages image-related operations, such as generating images and fetching random images from Unsplash.
    """

    @staticmethod
    def get_together_api_key() -> Optional[str]:
        """
        Retrieve the Together API key from the configuration.

        Returns:
            str or None: The Together API key if available, or None if no key is set.
        """
        return ConfigManager.get_together_api_key()

    @staticmethod
    async def generate_image(prompt: str, width: int = 1024, height: int = 768, steps: int = 28) -> Optional[str]:
        """
        Generate an image from a text prompt.

        Args:
            prompt (str): The text prompt to generate an image.
            width (int): The width of the generated image.
            height (int): The height of the generated image.
            steps (int): The number of steps for image generation.

        Returns:
            str: The path of the saved generated image or None if failed.
        """
        api_key = ImageManager.get_together_api_key()
        if not api_key:
            raise ValueError("Together API key is not provided in the configuration.")

        client = Together(api_key=api_key)

        try:
            response = await asyncio.to_thread(
                client.images.generate,
                prompt=prompt,
                model="black-forest-labs/FLUX.1-pro",
                width=width,
                height=height,
                steps=steps,
                n=1,
                response_format="b64_json"
            )

            if not response or not response.data or not response.data[0].b64_json:
                return None

            return await ImageManager.save_image(response.data[0].b64_json)
        except Exception as e:
            print(f"Error generating image: {e}")
            return None

    @staticmethod
    async def save_image(base64_data: str) -> str:
        """
        Save a base64 encoded image to a file.

        Args:
            base64_data (str): Base64 encoded image data.

        Returns:
            str: The path of the saved image.
        """
        output_dir = "./.temp"
        await aiofiles.os.makedirs(output_dir, exist_ok=True)

        image_data = base64.b64decode(base64_data)
        image_path = os.path.join(output_dir, f"generated_image_{os.urandom(4).hex()}.png")

        async with aiofiles.open(image_path, "wb") as f:
            await f.write(image_data)

        return image_path

    @staticmethod
    async def get_image(query: Optional[str] = None) -> Optional[str]:
        """
        Asynchronously fetch a random image from Unsplash. Optionally, a query can be passed 
        to specify the image theme.

        Args:
            query (str, optional): Search query to fetch a specific type of image. If not provided, 
                                   a completely random image is fetched.

        Returns:
            str: The URL of the fetched image, or an error message if the fetch failed.
        """
        access_key = ImageManager._get_access_key()
        if not access_key:
            raise ValueError("Unsplash API key is not provided in the configuration.")

        params: Dict[str, Any] = {"client_id": access_key}
        if query:
            params["query"] = query

        try:
            async with aiohttp.ClientSession(timeout=ClientTimeout(total=10)) as session:
                async with session.get("https://api.unsplash.com/photos/random", params=params) as response:
                    response.raise_for_status()
                    data = await response.json()
                    image_url = data.get("urls", {}).get("regular")

                    if not image_url:
                        raise ValueError("No image URL found in the response from Unsplash.")

                    return image_url

        except aiohttp.ClientError as e:
            print(f"Error making request to Unsplash API: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    @staticmethod
    def _get_access_key() -> Optional[str]:
        """
        Retrieve the appropriate Unsplash API access key from the configuration.

        Returns:
            str or None: The Unsplash access key if available, or None if no key is set.
        """
        return ConfigManager.get_unsplash_key2() if ConfigManager.using_unsplash_key2() else ConfigManager.get_unsplash_key()
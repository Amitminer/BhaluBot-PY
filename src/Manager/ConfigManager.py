import os
import yaml
from typing import Union, Optional, Dict


class ConfigManager:
    """
    Manages configuration settings for the bot.
    """

    CONFIG_FILE_PATH = "config.yml"

    @staticmethod
    def load_config() -> Optional[Dict]:
        """
        Load the configuration settings from the config file.
        """
        config_file_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "..", ConfigManager.CONFIG_FILE_PATH
            )
        )

        try:
            with open(config_file_path, "r") as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"Error loading config file: {e}")
            return None

    @staticmethod
    def get_config_value(value: str) -> Union[str, int, Dict[str, str], None]:
        """
        Get a specific value from the configuration settings.
        """
        config = ConfigManager.load_config()
        return config.get(value) if config else None

    @staticmethod
    def get_prefix() -> str:
        """
        Get the command prefix from the configuration settings.
        If prefix is invalid, use '+' as default.
        """
        prefix = ConfigManager.get_config_value("Prefix")
        return prefix if prefix else "+"

    @staticmethod
    def get_authors() -> Dict:
        """
        Get the authors and their corresponding IDs from the configuration settings.
        """
        authors = ConfigManager.get_config_value("owner-ids")
        return authors if isinstance(authors, dict) else {}

    @staticmethod
    def using_unsplash_key2() -> Optional[bool]:
        """
        Check if the bot is using the second Unsplash key.
        """
        return ConfigManager.get_config_value("Use_Unsplash_key2")

    @staticmethod
    def get_gemini_settings() -> Dict:
        """
        Get the Gemini settings from the configuration.
        """
        return {
            "generation_config": ConfigManager.get_config_value("generation_config"),
            "safety_settings": ConfigManager.get_config_value("safety_settings"),
        }

    @staticmethod
    def get_chatgpt_api() -> Optional[str]:
        """
        Get the ChatGPT API access token from environment variables.
        """
        return os.getenv("CHATGPT_ACCESS_TOKEN")

    @staticmethod
    def get_openai_key() -> Optional[str]:
        """
        Get the OpenAI API key from environment variables.
        """
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_unsplash_key() -> Optional[str]:
        """
        Get the Unsplash API access key from environment variables.
        """
        return os.getenv("UNSPLASH_ACCESS_KEY")

    @staticmethod
    def get_unsplash_key2() -> Optional[str]:
        """
        Get the second Unsplash API access key from environment variables.
        """
        return os.getenv("UNSPLASH_ACCESS_KEY_2")

    @staticmethod
    def get_geminiAi_key() -> Optional[str]:
        """
        Get the Google Generative AI API access key from environment variables.
        """
        return os.getenv("GEMINIAI_KEY")

    @staticmethod
    def get_bot_token() -> str:
        """
        Get the Discord bot token from environment variables.
        Raise an error if the token is invalid.
        """
        bot_token = os.getenv("DISCORD_BOT_TOKEN")
        if not bot_token:
            raise ValueError("Discord bot token is not provided.")
        return bot_token

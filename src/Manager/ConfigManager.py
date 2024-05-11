import os
import yaml
from typing import Union, Optional

class ConfigManager:
    CONFIG_FILE_PATH = 'config.yml'

    def __init__(self):
        pass

    @staticmethod
    def load_config() -> Optional[dict]:
        config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', ConfigManager.CONFIG_FILE_PATH))
    
        try:
            with open(config_file_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f'Error loading config file: {e}')
            return None

    @staticmethod
    def get_config_value(value: str) -> Union[str, int, dict[str, str], None]:
        config = ConfigManager.load_config()
        return config[value] if config else None

    @staticmethod
    def get_prefix() -> Optional[str]:
        return ConfigManager.get_config_value("Prefix")

    @staticmethod
    def get_authors() -> dict[str, str]:
        authors = ConfigManager.get_config_value("author-Id")
        return authors if isinstance(authors, dict) else {}

    @staticmethod
    def get_chatgpt_api() -> Optional[str]:
        return os.getenv('CHATGPT_ACCESS_TOKEN', None)

    @staticmethod
    def get_openai_key() -> Optional[str]:
        return os.getenv('OPENAI_API_KEY', None)

    @staticmethod
    def get_unsplash_key() -> Optional[str]:
        return os.getenv('UNSPLASH_ACCESS_KEY', None)

    @staticmethod
    def get_bot_token() -> Optional[str]:
        return os.getenv('DISCORD_BOT_TOKEN', None)
import os
import yaml
from typing import Union, Optional

class ConfigManager:
    """
    Manages configuration settings for the bot.
    """
    CONFIG_FILE_PATH = 'config.yml'

    def __init__(self):
        pass

    @staticmethod
    def load_config() -> Optional[dict]:
        """
        Load the configuration settings from the config file.
        """
        config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', ConfigManager.CONFIG_FILE_PATH))

        try:
            with open(config_file_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f'Error loading config file: {e}')
            return None

    @staticmethod
    def get_config_value(value: str) -> Union[str, int, dict[str, str], None]:
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
        return prefix if prefix else '+'

    @staticmethod
    def get_authors() -> dict:
        """
        Get the authors and their corresponding IDs from the configuration settings.
        """
        authors = ConfigManager.get_config_value("author-Id")
        return authors if isinstance(authors, dict) else {}

    @staticmethod
    def get_chatgpt_api() -> Optional[str]:
        """
        Get the ChatGPT API access token from environment variables.
        """
        return os.getenv('CHATGPT_ACCESS_TOKEN')

    @staticmethod
    def get_openai_key() -> Optional[str]:
        """
        Get the OpenAI API key from environment variables.
        """
        return os.getenv('OPENAI_API_KEY')

    @staticmethod
    def get_unsplash_key() -> Optional[str]:
        """
        Get the Unsplash API access key from environment variables.
        """
        return os.getenv('UNSPLASH_ACCESS_KEY')

    @staticmethod
    def get_bot_token() -> str:
        """
        Get the Discord bot token from environment variables.
        Raise an error if the token is invalid.
        """
        bot_token = os.getenv('DISCORD_BOT_TOKEN')
        if not bot_token:
            raise ValueError("Discord bot token is not provided.")
        return bot_token

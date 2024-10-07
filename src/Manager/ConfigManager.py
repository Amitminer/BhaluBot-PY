import os
import yaml
from typing import Union, Optional, Dict, Any


class ConfigManager:
    """
    Manages configuration settings for the bot, including loading configuration files and retrieving 
    values for various settings such as API keys, bot tokens, and other custom configurations.
    """

    CONFIG_FILE_PATH = "config.yml"
    DEFAULT_GEMINI_MODEL_ID = "gemini-1.5-flash-latest"
    
    @staticmethod
    def load_config() -> Optional[Dict[str, Any]]:
        """
        Load the configuration settings from the YAML config file.
        
        Returns:
            dict: A dictionary containing the configuration settings if the file loads successfully.
            None: If there is an error loading the config file.
        """
        config_file_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "..", ConfigManager.CONFIG_FILE_PATH
            )
        )

        try:
            with open(config_file_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Config file not found at {config_file_path}")
            return None
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error while loading config file: {e}")
            return None

    @staticmethod
    def get_config_value(key: str) -> Optional[Union[str, int, Dict[str, Any]]]:
        """
        Retrieve a specific value from the configuration settings.

        Args:
            key (str): The key for the configuration setting to retrieve.

        Returns:
            Union[str, int, dict, None]: The value associated with the key, or None if the key is not found.
        """
        config = ConfigManager.load_config()
        return config.get(key) if config else None

    @staticmethod
    def get_prefix() -> str:
        """
        Retrieve the command prefix for the bot.

        Returns:
            str: The command prefix, or '+' if the prefix is not set in the configuration.
        """
        return ConfigManager.get_config_value("Prefix") or "+"

    @staticmethod
    def get_authors() -> Dict[str, str]:
        """
        Retrieve the authors (owners) and their corresponding IDs from the configuration.

        Returns:
            dict: A dictionary where keys are author names and values are their IDs.
        """
        authors = ConfigManager.get_config_value("owner-ids")
        return authors if isinstance(authors, dict) else {}

    @staticmethod
    def using_unsplash_key2() -> Optional[bool]:
        """
        Check if the bot is configured to use the second Unsplash API key.

        Returns:
            bool or None: True if using the second key, False if not, None if not configured.
        """
        return ConfigManager.get_config_value("Use_Unsplash_key2")

    @staticmethod
    def get_gemini_settings() -> Dict[str, Any]:
        """
        Retrieve the Gemini AI generation and safety settings from the configuration.

        Returns:
            dict: A dictionary containing 'generation_config' and 'safety_settings' keys.
        """
        return {
            "generation_config": ConfigManager.get_config_value("generation_config"),
            "safety_settings": ConfigManager.get_config_value("safety_settings"),
        }

    @staticmethod
    def get_finetune_prompt() -> Optional[list[str]]:
        """
        Retrieve the list of fine-tuned prompts from the configuration.

        Returns:
            list[str]: A list of fine-tuned prompts, or an empty list if not configured.
        """
        fine_tune = ConfigManager.get_config_value("fine_tune")
        return fine_tune.get('prompt', []) if fine_tune else []

    @staticmethod
    def get_chatgpt_api() -> Optional[str]:
        """
        Retrieve the ChatGPT API access token from environment variables.

        Returns:
            str or None: The ChatGPT API token if found, else None.
        """
        return os.getenv("CHATGPT_ACCESS_TOKEN")

    @staticmethod
    def get_openai_key() -> Optional[str]:
        """
        Retrieve the OpenAI API key from environment variables.

        Returns:
            str or None: The OpenAI API key if found, else None.
        """
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_unsplash_key() -> Optional[str]:
        """
        Retrieve the Unsplash API access key from environment variables.

        Returns:
            str or None: The Unsplash API access key if found, else None.
        """
        return os.getenv("UNSPLASH_ACCESS_KEY")

    @staticmethod
    def get_unsplash_key2() -> Optional[str]:
        """
        Retrieve the second Unsplash API access key from environment variables.

        Returns:
            str or None: The second Unsplash API access key if found, else None.
        """
        return os.getenv("UNSPLASH_ACCESS_KEY_2")
    
    @staticmethod
    def get_together_api_key() -> Optional[str]:
        """
        Retrieve the Together API key from environment variables.

        Returns:
            str or None: The Together API access key if found, else None.
        """
        return os.getenv("TOGETHER_API_KEY")

    @staticmethod
    def get_geminiAi_key() -> Optional[str]:
        """
        Retrieve the Google Generative AI (Gemini AI) API access key from environment variables.

        Returns:
            str or None: The Gemini AI API key if found, else None.
        """
        return os.getenv("GEMINIAI_KEY")
    
    @staticmethod
    def get_gemini_model_id() -> str:
        """
        Retrieve the Gemini AI model ID from the configuration.
        If not set, return the default model ID.

        Returns:
            str: The model ID for Gemini AI, or the default model ID if not found.
        """
        return ConfigManager.get_config_value("gemini_model_id") or ConfigManager.DEFAULT_GEMINI_MODEL_ID


    @staticmethod
    def get_bot_token() -> str:
        """
        Retrieve the Discord bot token from environment variables.
        
        Returns:
            str: The Discord bot token.
        
        Raises:
            ValueError: If the Discord bot token is not provided.
        """
        bot_token = os.getenv("DISCORD_BOT_TOKEN")
        if not bot_token:
            raise ValueError("Discord bot token is not provided.")
        return bot_token

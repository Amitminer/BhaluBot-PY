```markdown
# BhaluBot Discord Bot (Under Development)

BhaluBot is a versatile Discord bot designed to elevate your server experience with interactive and entertaining features. From generating random images to providing insightful responses, BhaluBot is here to make your Discord server lively and engaging.

**Please note: This bot is currently under development. More commands will be added soon.**

## Installation:

1. **Clone the repository:**
   ```
   git clone https://github.com/Amitminer/BhaluBot-PY.git
   cd BhaluBot
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Setup:**

   - **Configuration:**
     BhaluBot uses a `config.yml` file for configuration. Ensure the following settings are correctly configured in the `config.yml`

   - **Environment Variables:**
     Create a `.env` file in the root directory to store your sensitive information. Here are the environment variables you can set in the `.env` file [Click me to see .env setup](https://github.com/Amitminer/BhaluBot-PY#environment-variables-env)

5. **Start the bot using:**

   ```bash
   ./start.sh
   ```
   or
   ```bash
   ./start.bat
   ```

## Commands:

- **`+random (your query)`**

  Generates a random image based on your query, for example:
  ```
  +random supercar
  ```
  BhaluBot will send you a random supercar image. Powered by Unsplash API.

- **`+spam (count) (message to spam)`**

  Sends the specified message multiple times, for example:
  ```
  +spam 5 hello
  ```
  BhaluBot will send "hello" 5 times.

- **`+say (message)`**

  Bot will send the specified message, for example:
  ```
  +say Hello, everyone!
  ```
  BhaluBot will send "Hello, everyone!"

- **`+shutdown`**

  Shuts down the bot for maintenance. This command is owner-only.

## Configuration:

- **`config.yml`**

  ```yaml
  # Your bot prefix
  prefix: +
  ```
  
## Environment Variables (`.env`):

Create a `.env` file in the root directory to store your sensitive information. Here are the environment variables you can set in the `.env` file:

- `DISCORD_BOT_TOKEN`: Your Discord bot token.
- `OPENAI_API_KEY`: Your OpenAI API key. Get it from [OpenAI](https://platform.openai.com/).
- `UNSPLASH_ACCESS_KEY`: Your Unsplash API key. Obtain it from [Unsplash](https://unsplash.com/developers).
- `CHATGPT_ACCESS_TOKEN`: Your ChatGPT API access token.

Example `.env` file:

```plaintext
DISCORD_BOT_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
UNSPLASH_ACCESS_KEY=your_unsplash_access_key
CHATGPT_ACCESS_TOKEN=your_chatgpt_access_token
```

Make sure to replace `your_discord_bot_token`, `your_openai_api_key`, `your_unsplash_access_key`, and `your_chatgpt_access_token` with your actual tokens and keys.

These environment variables are crucial for the proper functioning of BhaluBot. Ensure that you keep this file secure and do not share these sensitive details publicly.


## Contributing:

If you find a bug or want to suggest an improvement, please feel free to open an issue or submit a pull request. Your contributions are greatly appreciated!

## License:

Bhalu Bot is open-source software licensed under the [MIT License](LICENSE).

## Credits:

The Bhalu Discord Bot is created and maintained by [AmitxD](https://github.com/Amitminer), based on BhaluBot (php).
```

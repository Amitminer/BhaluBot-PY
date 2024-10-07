# BhaluBot-PY

BhaluBot is a versatile Discord bot designed to elevate your server experience with interactive and entertaining features. From generating random images to providing insightful responses, BhaluBot is here to make your Discord server lively and engaging.

**Please note: This bot is currently under development. More commands will be added soon.**

## Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Amitminer/BhaluBot-PY.git
   cd BhaluBot
   ```

2. **Rename the `.env.example` file to `.env`:**
- Update the `.env` file with the following information:
   ```plaintext
   DISCORD_BOT_TOKEN=
   UNSPLASH_ACCESS_KEY=
   UNSPLASH_ACCESS_KEY_2=
   TOGETHER_API_KEY=
   GEMINIAI_KEY=
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup:**

   - **Configuration:**
     BhaluBot uses a `config.yml` file for configuration. Ensure the following settings are correctly configured in `config.yml`:

     ```yaml
     # config.yml
     
     # Prefix for bot commands
     Prefix: "++"

     # Owner ID of the bot (e.g., Discord user ID)
     owner_ids:
     - 814660125511778315

     gemini_model_id: "gemini-1.5-flash-002"
     # Generation configuration for the AI model
     generation_config:
       temperature: 1                    # Temperature parameter for text generation
       top_p: 0.95                           # Top p parameter for text generation
       top_k: 40                            # Top k parameter for text generation
       max_output_tokens: 2048             # Maximum number of output tokens
       response_mime_type: "text/plain"    # Mime type of the response

     # Safety settings for filtering harmful content
     safety_settings:
       - category: "HARM_CATEGORY_HARASSMENT"            # Category of harmful content (e.g., harassment)
         threshold: "BLOCK_NONE"                         # Threshold for blocking (e.g., none)
       - category: "HARM_CATEGORY_HATE_SPEECH"           # Category of harmful content (e.g., hate speech)
         threshold: "BLOCK_NONE"                         # Threshold for blocking (e.g., none)
       - category: "HARM_CATEGORY_SEXUALLY_EXPLICIT"     # Category of harmful content (e.g., sexually explicit)
         threshold: "BLOCK_NONE"                         # Threshold for blocking (e.g., none)
       - category: "HARM_CATEGORY_DANGEROUS_CONTENT"     # Category of harmful content (e.g., dangerous content)
         threshold: "BLOCK_NONE"                         # Threshold for blocking (e.g., none)

     # IF your primary unsplash API key limit is reached, use backup API instead.
     Use_Unsplash_key2: false

     fine_tune:
       prompt:
         - "Your custom data to fine tune ai chatbot"
     ```

5. **Start the bot using:**

   ```bash
   ./start.sh
   ```
   or
   ```bash
   ./start.bat
   ```

## Commands:

### Admin Commands:

- **`++ban @user1 @user2 {reason}`**  
  A simulated ban command for fun.

- **`++shutdown`**  
  Shuts down the bot for maintenance. This command is owner-only.

### Fun Commands:

- **`++ask {your message}`**  
  Ask the bot anything.

- **`++food [category]`**  
  Sends a random food image or an image from a specified category.

- **`++foodlist`**  
  Lists all available food categories.

- **`++hack @user`**  
  A prank simulation targeting a random user.

- **`++imagine {your prompt}`**  
  Generates an image based on your prompt using AI.

- **`++ship user1 user2`**  
  Ships two users together and generates a random compatibility percentage.

- **`++tts {lang} {text}`**  
  Generates a TTS audio file from the given text and sends it in the channel.

### General Commands:

- **`++ping`**  
  Shows the bot's current latency.

- **`++say {message}`**  
  Bot sends the specified message.

- **`++help`**  
  Lists all available commands.

### Utility Commands:

- **`++currency {country1} {country2} {amount}`**  
  Converts currency between two countries.

- **`++search {number} {your query}`**  
  Searches for a random image based on your query.

- **`++summarize {link}`**  
  Summarizes the content of the provided URL.

## Configuration:

- **`config.yml`**  
  See the configuration section above for details.

## Environment Variables (`.env`):

Ensure the following variables are set in your `.env` file:

- `DISCORD_BOT_TOKEN`: Your Discord bot token.
- `UNSPLASH_ACCESS_KEY`: Your Unsplash API key.
- `UNSPLASH_ACCESS_KEY_2`: A backup Unsplash API key (if needed).
- `TOGETHER_API_KEY`: Your Together API key.
- `GEMINIAI_KEY`: Your Gemini AI key.

## Contributing:

If you find a bug or want to suggest an improvement, please feel free to open an issue or submit a pull request. Your contributions are greatly appreciated!

## License:

Bhalu Bot is open-source software licensed under the [MIT License](LICENSE).

## Credits:

The Bhalu Discord Bot is created and maintained by [AmitxD](https://github.com/Amitminer), based on BhaluBot (PHP).

---
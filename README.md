# Twitch Watchtime Discord Rich Presence

This Python script is designed to connect to a Twitch channel's IRC (Internet Relay Chat) and track the watch time of a specific user. It utilizes the `socket` library for IRC communication, `pypresence` for Discord Rich Presence updates, and `schedule` for periodic task execution. The DiscordRP is fully customizable.

![Example](/images/githubimage.png)

## Features

- **IRC Connection:** Connects to Twitch IRC using your own Twitch account to receive chat messages. (No bot or server needed)
- **Watch Time Tracking:** Tracks the watch time of a specified user in the chat.
- **Discord Rich Presence:** Updates Discord Rich Presence with the total watch time.
- **Automatic Scheduling:** Periodically executes the watch time tracking function.

## Requirements

- Python 3
- `socket` library (standard in Python 3)
- `pypresence` (included in requirements.txt)
- `schedule` (included in requirements.txt)
- Twitch account and OAuth token: Go to https://twitchapps.com/tmi/ and connect your Twitch account. Generate the token and store it somewhere.
- A Discord application: Follow these instructions https://discord.com/developers/docs/getting-started

## Installation

1. Clone the repository or download the script. 
   ```bash
   git clone https://github.com/NxKW/DiscordTwitchRP.git

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt

## Usage
Replace the placeholder values in the script:

- BOT_USERNAME: Your Twitch username.
- CHANNEL_NAME: The Twitch channel you want to connect to.
- BOT_OAUTH_TOKEN: The OAuth token we generated earlier.
- client_id: Your Discord application's client ID (for Rich Presence).
- buttons: You can customize these buttons to your liking.
- Running the script: 
  ```bash 
  python3 start.pyw
- Alternatively: Create a Windows task in Task Scheduler that runs this script at log on of any user, delay the script by 10 minutes so you have time to startup Discord. The script will automatically run after these 10 minutes.


## IMPORTANT
**Make sure to replace all YOUR_TWITCH_USERNAME in the script with your own Twitch username in lowercase letters! I suggest you don't change the 'schedule.every(4).hours.do(execute_function)' to anything lower than 4 hours to prevent unintended chat spams.**

## Disclaimer
This bot is created as a fun and educational project. Users are advised to use it responsibly and in compliance with Twitch's Terms of Service and Community Guidelines. This bot should not be used for spamming, harassment, or any form of abusive behavior on Twitch's platform. The developer is not responsible for any misuse of the bot or any consequences that arise from such misuse. Always ensure your usage of the bot respects the rights and experience of the Twitch community. Thank you.

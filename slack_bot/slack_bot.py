import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# For local development, you'd typically load this from environment variables
# SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
# SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

# Placeholder for your bot token (replace with your actual token)
SLACK_BOT_TOKEN = "xoxb-YOUR-BOT-TOKEN"

client = WebClient(token=SLACK_BOT_TOKEN)

def send_message(channel_id, message):
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print(f"Message sent: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

if __name__ == "__main__":
    print("This is a basic Slack Bot example.")
    print("To make it functional, you need to:")
    print("1. Create a Slack App (api.slack.com/apps)")
    print("2. Install the app to your workspace.")
    print("3. Get your Bot User OAuth Token (xoxb-...) and replace 'xoxb-YOUR-BOT-TOKEN'.")
    print("4. Enable Socket Mode and get an App-Level Token (xapp-...).")
    print("5. Subscribe to events (e.g., app_mention, message.channels).")
    print("6. Run this script and use a tool like Ngrok to expose it to Slack.")
    print("   (e.g., python -m slack_bolt.adapter.socket_mode run --app-file your_bot_file.py)")
    print("   This script only demonstrates sending a message.")

    # Example usage (replace with a real channel ID from your workspace)
    # channel_id = "C0XXXXXXX" # e.g., a channel where your bot is invited
    # send_message(channel_id, "Hello from your new Python bot!")

import os
from slack_bolt import App
from dotenv import load_dotenv
from .command_handler import handle_claude_command # Relative import

load_dotenv() # Load .env file

# Initialize Bolt App for Claude Engineer
app = App(
    token=os.getenv("SLACK_CLAUDE_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_CLAUDE_SIGNING_SECRET")
)

# Command handler for /claude
@app.command("/claude")
def slack_command_claude(ack, respond, command):
    ack()
    user_input = command["text"]
    result = handle_claude_command(user_input)
    respond(result)

# Event handler for mentions specific to Claude
@app.event("app_mention")
def handle_claude_mention(body, say, context):
    event = body["event"]
    bot_user_id = context.bot_user_id # Get this bot's user ID
    text = event["text"]
    user_id = event["user"]

    # Check if this specific bot was mentioned
    if f"<@{bot_user_id}>" in text:
        # Remove the mention part to get the actual user input
        user_input = text.split(f"<@{bot_user_id}>", 1)[-1].strip()
        if user_input: # Respond only if there's text after the mention
             result = handle_claude_command(user_input)
             say(text=f"<@{user_id}> {result}", thread_ts=event.get("thread_ts", event.get("ts")))
        else:
             # Optional: Respond to mention without text
             say(text=f"Hola <@{user_id}>! Soy Claude Engineer. ¿En qué puedo ayudarte? Puedes usar /claude [tu solicitud].", thread_ts=event.get("thread_ts", event.get("ts")))

# Note: No need for __main__ block if started from main.py

from slack_bolt import App
import os

# Importar los handlers de cada agente
from interface.slack_claude.command_handler import handle_claude_command
from interface.slack_storm.command_handler import handle_storm_command

app = App(
    token=os.getenv("SLACK_CLAUDE_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_CLAUDE_SIGNING_SECRET")
)

@app.command("/claude")
def slack_command_claude(ack, respond, command):
    ack()
    user_input = command["text"]
    result = handle_claude_command(user_input)
    respond(result)

@app.command("/storm")
def slack_command_storm(ack, respond, command):
    ack()
    user_input = command["text"]
    result = handle_storm_command(user_input)
    respond(result)

# Event handler for app mentions
@app.event("app_mention")
def handle_app_mention_events(body, say):
    event = body["event"]
    text = event["text"]
    user_id = event["user"] # ID of the user who mentioned the bot

    # Simple routing based on keywords in the mention text
    # A more robust approach might check the mentioned bot's user ID
    if "claude" in text.lower():
        # Remove the mention part to get the actual user input
        user_input = text.split(">", 1)[-1].strip()
        result = handle_claude_command(user_input)
        say(text=f"<@{user_id}> {result}") # Mention the user back
    elif "storm" in text.lower():
        # Remove the mention part to get the actual user input
        user_input = text.split(">", 1)[-1].strip()
        result = handle_storm_command(user_input)
        say(text=f"<@{user_id}> {result}") # Mention the user back
    else:
        # Default response if no specific bot keyword is found
        say(text=f"Hola <@{user_id}>! ¿En qué puedo ayudarte? Puedes usar /claude o /storm.")

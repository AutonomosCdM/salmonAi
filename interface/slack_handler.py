from slack_bolt import App
import os

# Importar los handlers de cada agente
from interface.slack_claude.command_handler import handle_claude_command
from interface.slack_storm.command_handler import handle_storm_command

app = App(
    token=os.getenv("SLACK_CLAUDE_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_CLAUDE_SIGNING_SECRET"),
    app_token=os.getenv("SLACK_CLAUDE_APP_TOKEN")
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

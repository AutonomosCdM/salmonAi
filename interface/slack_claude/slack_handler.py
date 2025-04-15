# Slack Handler para Claude Engineer
from slack_bolt import App
import os

app = App(
    token=os.getenv("SLACK_CLAUDE_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_CLAUDE_SIGNING_SECRET"),
    app_token=os.getenv("SLACK_CLAUDE_APP_TOKEN")
)

@app.command("/claude")
def handle_claude_command(ack, respond, command):
    ack()
    user_input = command["text"]
    response = f"Claude Engineer recibió tu solicitud: {user_input}"
    respond(response)
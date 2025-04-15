# Slack Handler para Storm Scientist
from slack_bolt import App
import os

app = App(
    token=os.getenv("SLACK_STORM_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_STORM_SIGNING_SECRET"),
    app_token=os.getenv("SLACK_STORM_APP_TOKEN")
)

@app.command("/storm")
def handle_storm_command(ack, respond, command):
    ack()
    user_input = command["text"]
    response = f"Storm Scientist recibió tu solicitud: {user_input}"
    respond(response)
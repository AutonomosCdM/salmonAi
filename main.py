import os
from agents.claude_engineer import ClaudeEngineer
from agents.storm_scientist import StormScientist
from interface.cli_chat.cli_handler import chat_interface

from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler # Import SocketModeHandler

# Import individual Slack handlers
from interface.slack_claude.slack_handler import app as claude_app
from interface.slack_storm.slack_handler import app as storm_app

load_dotenv()  # Load environment variables from .env file

# Init agents
claude = ClaudeEngineer()
storm = StormScientist()
AGENTS = {"claude": claude, "storm": storm}

load_dotenv(override=True) # Explicitly reload and override
MODE = os.getenv("APP_MODE", "cli").strip()
AGENT_NAME = os.getenv("AGENT_NAME", "claude").strip() # Default to claude if not set

if __name__ == "__main__":
    if MODE == "cli":
        chat_interface(AGENTS)
    elif MODE == "cli_remote":
        print("CLI remoto activado (simulado)")
        while True:
            user_input = input("remote> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            print(chat_interface(AGENTS, user_input))
    elif MODE == "slack":
        if AGENT_NAME == "claude":
            app_token = os.getenv("SLACK_CLAUDE_APP_TOKEN")
            if not app_token:
                print("Error: SLACK_CLAUDE_APP_TOKEN no está configurado.")
            else:
                print("Iniciando Slack app para Claude Engineer via Socket Mode...")
                SocketModeHandler(claude_app, app_token).start()
        elif AGENT_NAME == "storm":
            app_token = os.getenv("SLACK_STORM_APP_TOKEN")
            if not app_token:
                print("Error: SLACK_STORM_APP_TOKEN no está configurado.")
            else:
                print("Iniciando Slack app para Storm Scientist via Socket Mode...")
                SocketModeHandler(storm_app, app_token).start()
        else:
            print(f"AGENT_NAME inválido: {AGENT_NAME}. Usa 'claude' o 'storm'.")
    else:
        print(f"APP_MODE inválido: {MODE}. Usa 'cli', 'cli_remote' o 'slack'.")

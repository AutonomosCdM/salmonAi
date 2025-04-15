import os
from agents.claude_engineer import ClaudeEngineer
from agents.storm_scientist import StormScientist
from interface.cli_chat import chat_interface
from interface.cli_handler import run_command

# Slack handlers (carga condicional)
from interface.slack_claude.slack_handler import app as claude_app
from interface.slack_storm.slack_handler import app as storm_app

# Init agents
claude = ClaudeEngineer()
storm = StormScientist()
AGENTS = {"claude": claude, "storm": storm}

MODE = os.getenv("APP_MODE", "cli")  # Valores posibles: cli, cli_remote, slack

if __name__ == "__main__":
    if MODE == "cli":
        chat_interface(AGENTS)
    elif MODE == "cli_remote":
        print("CLI remoto activado (simulado)")
        while True:
            user_input = input("remote> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            print(run_command(AGENTS, user_input))
    elif MODE == "slack":
        print("Slack apps activadas (Claude & Storm)")
        claude_app.start(port=int(os.getenv("PORT", 3000)))
        storm_app.start(port=int(os.getenv("PORT", 3001)))
    else:
        print("APP_MODE inválido. Usa cli, cli_remote o slack.")
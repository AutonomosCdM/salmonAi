import os
from agents.claude_engineer import ClaudeEngineer
from agents.storm_scientist import StormScientist
from interface.cli_chat import chat_interface
from interface.cli_handler import run_command
from dotenv import load_dotenv

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
            print(run_command(AGENTS, user_input))
    elif MODE == "slack":
        port = int(os.getenv("PORT", 3000))
        if AGENT_NAME == "claude":
            print(f"Iniciando Slack app para Claude Engineer en puerto {port}...")
            claude_app.start(port=port)
        elif AGENT_NAME == "storm":
            print(f"Iniciando Slack app para Storm Scientist en puerto {port}...")
            # Note: Running two apps on the same port locally might cause issues.
            # Railway will handle separate instances.
            storm_app.start(port=port)
        else:
            print(f"AGENT_NAME inválido: {AGENT_NAME}. Usa 'claude' o 'storm'.")
    else:
        print(f"APP_MODE inválido: {MODE}. Usa 'cli', 'cli_remote' o 'slack'.")

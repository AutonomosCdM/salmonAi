from agents.claude_engineer import ClaudeEngineer
from agents.storm_scientist import StormScientist
from interface.cli_chat import chat_interface

# Init agents
claude = ClaudeEngineer()
storm = StormScientist()

# Orchestrator
AGENTS = {
    "claude": claude,
    "storm": storm
}

if __name__ == "__main__":
    chat_interface(AGENTS)
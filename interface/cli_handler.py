# CLI Handler para ejecutar comandos desde consola remota o sistemas externos

def run_command(agent, command: str) -> str:
    if "storm" in command.lower():
        return agent["storm"].investigate(command)
    else:
        return agent["claude"].generate_roadmap(command)
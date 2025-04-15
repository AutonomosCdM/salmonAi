import os
from rich.console import Console

console = Console()

def chat_interface(agents: dict):
    console.print("[green]Bienvenido al mini demo conversacional de Claude Engineer & Storm[/]")
    console.print("[green]Escribe 'exit' para salir[/]")

    while True:
        try:
            user_input = input("[blue]Humano: [/]")
        except EOFError:
            console.print("Fin de la sesión.")
            break

        if user_input.lower() == "exit":
            console.print("Adiós!")
            break

        response = "[red]Por favor, especifica el agente (ej: 'claude: tu mensaje' o 'storm: tu mensaje').[/]"
        agent_prefix = ""
        actual_input = ""

        if ":" in user_input:
            parts = user_input.split(":", 1)
            agent_prefix = parts[0].strip().lower()
            actual_input = parts[1].strip()

            if agent_prefix == "claude" and "claude" in agents:
                # Assuming claude agent might have a more general method,
                # let's try calling a hypothetical 'process' method or default to roadmap
                if hasattr(agents["claude"], 'process'):
                     response = agents["claude"].process(actual_input)
                else:
                     response = agents["claude"].generate_roadmap(actual_input) # Fallback
            elif agent_prefix == "storm" and "storm" in agents:
                response = agents["storm"].investigate(actual_input)
            else:
                response = f"[red]Agente '{agent_prefix}' no reconocido. Usa 'claude' o 'storm'.[/]"
        else:
            # Keep the default message if no prefix is used
            pass

        console.print(f"[green]Agente: [/]{response}")
        console.print("-" * 40)  # Separator line

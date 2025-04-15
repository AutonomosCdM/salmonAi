def chat_interface(agents):
    """Interactive CLI interface for chatting with agents"""
    print("Bienvenido al mini demo conversacional de Claude Engineer & Storm")
    print("Escribe 'exit' para salir")
    
    while True:
        user_input = input("Humano: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        if "storm" in user_input.lower():
            response = agents["storm"].investigate(user_input)
        else:
            response = agents["claude"].generate_roadmap(user_input)
        
        print(f"Respuesta: {response}")

def run_command(agents, command: str) -> str:
    """Single command execution mode"""
    if "storm" in command.lower():
        return agents["storm"].investigate(command)
    else:
        return agents["claude"].generate_roadmap(command)

# Claude Engineer Command Handler

def handle_claude_command(user_input: str) -> str:
    # Aquí puedes llamar a la clase ClaudeEngineer real si lo necesitas
    # Por ahora un mock simple:

    if "roadmap" in user_input.lower():
        return "Claude Engineer está generando el roadmap solicitado..."
    else:
        return f"Claude Engineer recibió tu solicitud: {user_input}"

# Storm Scientist Command Handler

def handle_storm_command(user_input: str) -> str:
    # Aquí puedes llamar a la clase StormScientist real si lo necesitas
    # Por ahora un mock simple:

    if "investigar" in user_input.lower():
        return "Storm Scientist está investigando sobre el tema solicitado..."
    else:
        return f"Storm Scientist recibió tu solicitud: {user_input}"

def chat_interface(agents: dict):
    print("Bienvenido al mini demo conversacional de Claude Engineer & Storm")
    print("Escribe 'exit' para salir")

    while True:
        try:
            user_input = input("Humano: ")
        except EOFError:
            print("Fin de la sesión.")
            break

        if user_input.lower() == "exit":
            print("Adiós!")
            break

        response = ""

        if "storm" in user_input.lower():
            response = agents["storm"].investigate(user_input)
        else:
            response = agents["claude"].generate_roadmap(user_input)

        print(f"Agente: {response}")
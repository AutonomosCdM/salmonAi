def chat_interface(agents: dict):
    print("Bienvenido al mini demo conversacional de Claude Engineer & Storm")
    print("Escribe 'exit' para salir")

    while True:
        user_input = input("Humano: ")
        if user_input.lower() == "exit":
            print("Adiós!")
            break

        if "storm" in user_input.lower():
            response = agents["storm"].investigate("Cataratas en salmón")
        else:
            response = agents["claude"].generate_roadmap("Bolty Agent")

        print(f"Agente: {response}")
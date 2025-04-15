from tools.llm_engine import ask_llm
import os

class ClaudeEngineer:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "groq")

    def generate_roadmap(self, project_name: str) -> str:
        prompt = f"Actúa como DevOps. Crea un roadmap técnico para el proyecto {project_name}."
        return ask_llm(self.provider, prompt)
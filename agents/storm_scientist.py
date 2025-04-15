from core.llm_engine import ask_llm
import os

class StormScientist:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "groq")

    def investigate(self, topic: str) -> str:
        prompt = f"Actúa como científico. Investiga causas y efectos del tema: {topic}."
        response = ask_llm(self.provider, prompt)
        # Remove bold formatting (asterisks)
        response = response.replace("*", "").replace("**", "")
        return response

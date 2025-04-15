from tools.llm_engine import ask_llm
import os

class StormScientist:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "groq")

    def investigate(self, topic: str) -> str:
        prompt = f"Actúa como científico. Investiga causas y efectos del tema: {topic}."
        return ask_llm(self.provider, prompt)
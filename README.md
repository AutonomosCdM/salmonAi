# Mini Demo - Claude Engineer & Storm Agents

Este proyecto es un demo conversacional minimalista de arquitectura multi-agente, con integración de LLMs y despliegue Docker en Railway.

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Variables de entorno (.env)

```dotenv
GROQ_API_KEY=...
OPENAI_API_KEY=...
CLAUDE_API_KEY=...
LLM_PROVIDER=groq
```

## Despliegue en Railway

```bash
railway init
railway up
```

Listo para producción con Docker.
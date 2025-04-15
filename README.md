# SalmonAi — Multi-Agent Research System

SalmonAi es una plataforma modular de agentes AI diseñada para investigación científica y desarrollo técnico. Incluye dos agentes principales: Claude Engineer (IT) y Storm Scientist (Científico), cada uno desplegable vía Slack, CLI y Docker.

## Agentes
- **Claude Engineer**: Especialista en infraestructura, testing, roadmap y ejecución técnica.
- **Storm Scientist**: Especialista en investigación científica, hallazgos y validación.

## Modos de operación
- CLI local
- CLI remoto (simulación)
- Slack con Socket Mode
- Próximamente: Web/API

## Estructura del Proyecto

```
/salmonAi
├── agents/                    # Lógica de cada agente
│   ├── claude_engineer.py
│   └── storm_scientist.py
│
├── interface/                 # Entrada/Salida CLI & Slack
│   ├── cli_chat/
│   │   └── cli_handler.py
│   ├── slack_claude/
│   │   └── slack_handler.py
│   ├── slack_storm/
│   │   └── slack_handler.py
│
├── core/                      # Utilidades comunes (LLM)
│   └── llm_engine.py
│
├── memoryBank/                # Documentación de memoria
│   ├── README.md
│   ├── activeContext.md
│   └── data/                  # PDFs o docs internos
│
├── docs/                      # Documentación técnica
│   ├── architecture.md
│   ├── agents.md
│   └── memoryBank.md
```

Ver detalles en `docs/architecture.md`

## Setup Rápido

```bash
# 1. Clonar el repo
git clone <repo>

# 2. Crear entorno
python -m venv .venv && source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar CLI
python main.py
```

## Deploy Railway
- `Dockerfile` + `Procfile` listos
- `.env` por agente
- Usa `AGENT_NAME=claude` o `storm`

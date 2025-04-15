# Memory Bank — SalmonAi

Esta carpeta contiene toda la lógica de memoria persistente para los agentes AI.

## Objetivo
Proveer una capa de persistencia contextual, almacenando:
- Conversaciones por agente
- Logs por usuario
- Memoria para RAG (próximamente)

## Estructura
- `supabase_client.py`: conexión global a Supabase
- `memory_manager.py`: funciones de almacenamiento y recuperación

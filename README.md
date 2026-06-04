# Kafka-Hops

Demo de mensajería distribuida con Apache Kafka donde los mensajes "saltan" (hop) entre máquinas y topics:

- **Producer.js** — Productor Node.js que envía al topic `factory`
- **Producer&Consumer.py** — Middleware Python que consume `factory` y reenvía a `factory_response`
- **Consumer.py** — Consumidor final que lee `factory_response`

## Diagrama de arquitectura

```
[Node.js Producer] --> [topic: factory] --> [Python Middleware] --> [topic: factory_response] --> [Python Consumer]
   (Producer.js)                           (Producer&Consumer.py)                                   (Consumer.py)
```

## Prerrequisitos

- Docker y Docker Compose
- Node.js — instalar dependencias con `npm install`
- Python 3 — instalar dependencia con `pip install confluent-kafka`

## Configuración de red

Hay IPs hardcodeadas que deben ajustarse antes de correr el proyecto:

- En `Producer.js` línea 6: cambiar `192.168.68.55:9094` a la IP de la máquina que corre Kafka
- En `compose-demo/compose.yaml` línea 24: cambiar `192.168.68.59:9094` a la IP local de la máquina del broker

## Cómo correrlo

```bash
# 1. Levantar Kafka
cd compose-demo && docker compose up -d

# 2. Activar el entorno virtual
# Windows:
.\.venv\Scripts\Activate.ps1
# Mac/Linux:
source .venv/bin/activate

# 3. Correr el middleware (otra terminal)
python "Producer&Consumer.py"

# 4. Correr el consumidor final (otra terminal)
python Consumer.py

# 5. Enviar mensajes (otra terminal)
node Producer.js
```

## Tecnologías

- Apache Kafka — Confluent Platform 7.6, modo KRaft (sin ZooKeeper)
- Node.js + kafkajs
- Python + confluent-kafka

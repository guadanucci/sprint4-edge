# Projeto IoT – Passa a Bola  
Sprint 4: Aplicação Prática da Arquitetura IoT

---

# Sobre o Projeto

O Passa a Bola APP é um projeto que aplica a Internet das Coisas (IoT) ao esporte, simulando sensores instalados em bolas e coletes para coletar informações em tempo real durante treinos ou partidas.

O objetivo é permitir que treinadores e equipes possam analisar o desempenho dos atletas, monitorar sinais vitais e tomar decisões com base em dados reais.

Mesmo sem hardware físico, a comunicação é demonstrada via simulação em Python, que envia dados para o Node-RED através do protocolo MQTT.

---

# Arquitetura da Solução

Fluxo de funcionamento:


# Componentes Principais:
- **Python (paho-mqtt):** simula sensores IoT
- **Broker MQTT:** `broker.hivemq.com` (gratuito e público)
- **Node-RED:** recebe e exibe os dados em painéis (gauges e gráficos)
- **Dashboard:** visualiza velocidade da bola, batimentos cardíacos e impacto do chute

---

# Demonstração de Comunicação IoT

# Código Python (`simulador_passa_a_bola.py`)

O código simula os sensores e envia dados a cada 2 segundos:

# python
import time, random, json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "passa_a_bola/dados"

client = mqtt.Client("Simulador_Passa_a_Bola")
client.connect(BROKER, PORT, 60)

def gerar_dados():
    return {
        "velocidade_bola": round(random.uniform(30, 120), 2),
        "batimento_jogador": random.randint(60, 180),
        "impacto_chute": round(random.uniform(1.0, 10.0), 1)
    }

try:
    while True:
        dados = gerar_dados()
        payload = json.dumps(dados)
        client.publish(TOPIC, payload)
        print(f"📤 Dados enviados: {payload}")
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()
    print("🛑 Simulação encerrada.")

# Execução

pip install paho-mqtt

python simulador_passa_a_bola.py

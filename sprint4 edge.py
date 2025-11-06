# ---------------------------------------------------------
# PROJETO PASSA A BOLA APP - Simulação IoT com MQTT e Node-RED
# ---------------------------------------------------------
# Este script simula sensores de bola e colete enviando
# dados em tempo real via MQTT para um broker (HiveMQ, FIWARE etc.)
# ---------------------------------------------------------

import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "passa_a_bola/dados"

client = mqtt.Client("Simulador_Passa_a_Bola")

print("🔌 Conectando ao broker MQTT...")
client.connect(BROKER, PORT, 60)
print("✅ Conectado com sucesso!\n")

def gerar_dados():
    dados = {
        "velocidade_bola": round(random.uniform(30, 120), 2),
        "batimento_jogador": random.randint(60, 180),
        "impacto_chute": round(random.uniform(1.0, 10.0), 1)
    }
    return dados

try:
    while True:
        dados = gerar_dados()
        payload = json.dumps(dados)
        client.publish(TOPIC, payload)
        print(f"📤 Dados enviados: {payload}")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Simulação encerrada.")
    client.disconnect()

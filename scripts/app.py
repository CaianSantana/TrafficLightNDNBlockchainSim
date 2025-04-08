import threading
import time
import socket
import random
from fluxo import Fluxo
from semaforo import Semaforo
from multidao import Multidao
from transito import Transito

# Instância do semáforo
inicio = time.time()

semaforo = Semaforo()
multidao = Multidao(Fluxo.BAIXO)
transito = Transito(10, 2, 60, 8, Fluxo.MEDIO)


def tempo_atual():
    return int(time.time() - inicio)


def coordenar():
    while True:
        transito.chegar_carro()
        multidao.chegar_pedestre()
        if semaforo.cor_atual == "VERMELHO":
            transito.frear()
            multidao.atravessar()
        elif semaforo.cor_atual == "AMARELO":
            transito.reduzir()
        else:
            transito.avancar()
        time.sleep(1)


def enviar_mensagem(mensagem, tag, clock=0):
    """
    Envia uma mensagem para outro semáforo (simulado).
    
    Parâmetros:
    - mensagem: valor a ser enviado (ex: densidade ou tempo atual)
    - tag: tipo da mensagem ('DENSIDADE' ou 'SINCRONIA')
    - clock: tempo atual do semáforo (opcional, usado na sincronização)
    """
    pacote = {
        "tag": tag,
        "dados": mensagem,
        "clock": tempo_atual()
    }

    # Simulação de envio (substituir com NDNSim futuramente)
    print(f"📤 Enviando [{tag}] - Dados: {mensagem} | Clock: {clock}")

def escutar_mensagem(semaforo):

    while True:
        # Aqui simulamos a recepção da mensagem
        # No futuro, isso virá via NDNSim
        mensagem_recebida = {
            "tag": random.choice(["DENSIDADE", "SINCRONIA"]),
            "dados": random.randint(10, 30),  # pode ser densidade ou tempo
            "clock": random.randint(0, 5)
        }

        tag = mensagem_recebida["tag"]
        dados = mensagem_recebida["dados"]
        clock = mensagem_recebida["clock"]
        delay = tempo_atual() - clock

        if tag == "DENSIDADE":
            densidade_local = transito.get_densidade()
            if semaforo.avaliar(densidade_local, dados):
                semaforo.alterar_tempo(-5)
                print("✅ Cedeu tempo com base na densidade")
            else:
                semaforo.alterar_tempo(5)
                print("⏩ Manteve prioridade")
        
        elif tag == "SINCRONIA":
            semaforo.sincronizar(dados, delay)
            print(f"🔄 Sincronizado: tempo ajustado para {semaforo.tempo_restante}s")

        time.sleep(3)  # frequência de escuta



thread_tempo = threading.Thread(target=semaforo.contar_tempo)
thread_coordenador = threading.Thread(target=coordenar)
thread_comunicadora = threading.Thread(target=escutar_mensagem, args=(semaforo,))



thread_tempo.start()
thread_coordenador.start()
thread_comunicadora.start()
